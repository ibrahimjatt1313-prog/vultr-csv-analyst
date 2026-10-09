import os
import traceback
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("CRITICAL WARNING: GEMINI_API_KEY is missing or not loaded from .env file!")

client = genai.Client(api_key=api_key) if api_key else None

def generate_analysis_code(prompt: str, df_info: dict, model_name: str = "gemini-3-flash") -> str:
    try:
        if not client:
            return "# Error: GEMINI_API_KEY is missing in the .env file. Please add your key to continue."

        system_prompt = f"""
        You are an expert Python data analyst agent. 
        Dataset schema: {df_info}
        Write clean, executable Python code to solve the user's prompt. 
        Return ONLY valid Python code inside markdown blocks.
        """
        
        # Updated to gemini-3.8-flash as specified by Google API response
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=f"{system_prompt}\n\nUser Task: {prompt}"
        )
        
        code = response.text
        if not code:
            return "# Error: Model returned empty response."
            
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()
            
        return code
    except Exception as e:
        print(f"CRITICAL GEMINI ERROR: {str(e)}")
        traceback.print_exc()
        return f"# Error generating code: {str(e)}"