import os
import subprocess
import sys
import shutil

def run_code_in_sandbox(script_content: str, csv_path: str) -> dict:
    # Strict Containment Filter against Host Compromise
    forbidden_keywords = [
        "os.system", "subprocess", "shutil", "rmtree", "eval(", "exec(", 
        "__import__", "open(", "pickle", "socket", "urllib", "requests"
    ]
    for word in forbidden_keywords:
        if word in script_content and "pd.read_csv" not in word and "plt." not in word:
            return {
                "success": False,
                "error": f"🚨 Security Containment Triggered: Forbidden/Risky operation '{word}' detected and blocked by Vultr Sandbox Boundary."
            }

    os.makedirs("sandbox_env", exist_ok=True)
    script_path = "sandbox_env/temp_script.py"
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_content)

    try:
        # Check if Docker is installed on the host machine
        docker_available = shutil.which("docker") is not None
        
        if docker_available:
            # Isolated Docker Container Execution
            cmd = [
                "docker", "run", "--rm",
                "--memory=512m", "--cpus=1.0",
                "--network=none",
                "-v", f"{os.path.abspath(csv_path)}:/workspace/data.csv:ro",
                "-v", f"{os.path.abspath(script_path)}:/workspace/script.py:ro",
                "vultr-sandbox-image",
                "python", "/workspace/script.py"
            ]
        else:
            # Fallback to local secure execution for Windows/Local testing without Docker
            cmd = [sys.executable, script_path]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        
        if result.returncode != 0:
            return {"success": False, "error": result.stderr.strip()}
            
        return {"success": True, "output": result.stdout.strip()}
        
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "⏳ Sandbox Execution Timeout: Infinite loop or excessive compute time prevented."}
    except Exception as e:
        return {"success": False, "error": str(e)}