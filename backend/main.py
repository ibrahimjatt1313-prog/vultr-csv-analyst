from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import shutil
import os
import pandas as pd
from .agent import generate_analysis_code
from .sandbox import run_code_in_sandbox

app = FastAPI(title="Vultr CSV Analyst Agent API", version="2.0")
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    # Automatically serve frontend/index.html when opening localhost:8000
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/index.html"))
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Frontend index.html not found in frontend folder!</h3>"

@app.post("/api/analyze")
async def analyze_csv(
    file: UploadFile = File(...),
    prompt: str = Form(...),
    model: str = Form(default="llama-3.3-70b")
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        df = pd.read_csv(file_path)
        df_info = {
            "columns": list(df.columns),
            "dtypes": {str(k): str(v) for k, v in df.dtypes.items()},
            "sample": df.head(3).to_dict(orient="records")
        }
        
        code = generate_analysis_code(prompt, df_info, model_name=model)
        execution_result = run_code_in_sandbox(code, file_path)
        
        return JSONResponse(content={
            "success": True,
            "generated_code": code,
            "execution": execution_result
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))