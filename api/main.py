from fastapi import FastAPI, HTTPException
import subprocess
import asyncio
from pathlib import Path
from pydantic import BaseModel

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# スクリプトが保存されているディレクトリ（絶対パスで指定）
SCRIPT_DIRECTORY = Path(__file__).parent / "scripts"

# リクエストボディで受け取るデータモデル
class ScriptInput(BaseModel):
    language: str  # 実行言語
    input_value: str  # ユーザー入力を受け取るフィールド

# サポートされている言語とコマンドのマッピング
LANGUAGE_COMMANDS = {
    "python": ["python"],
    "javascript": ["node"],
    "typescript": ["ts-node"],
    "bash": ["bash"],
    "go": ["go", "run"],
    "cpp": ["g++", "-o", "temp_executable", "&&", "./temp_executable"],
    "ruby": ["ruby"],
    "java": ["java"],
    "php": ["php"],
    "perl": ["perl"]
}

# 非同期でスクリプトを実行する関数
async def run_script(command: list, script_path: Path, input_value: str):
    try:
        if "&&" in command:  # C++ のように複数コマンドが必要な場合
            compile_command = command[:3]
            execute_command = command[4:]

            # コンパイル
            compile_result = await asyncio.to_thread(subprocess.run, 
                                                     compile_command + [str(script_path)], 
                                                     text=True, capture_output=True)
            if compile_result.returncode != 0:
                raise HTTPException(status_code=500, detail=f"Compilation failed: {compile_result.stderr}")

            # 実行
            result = await asyncio.to_thread(subprocess.run, 
                                             execute_command, 
                                             text=True, capture_output=True, input=input_value, timeout=10)
        else:
            # 他の言語
            result = await asyncio.to_thread(subprocess.run, 
                                             command + [str(script_path)], 
                                             text=True, capture_output=True, input=input_value, timeout=10)

        return result
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Script execution timed out")
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Script execution failed with error: {e.stderr}")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Executable not found for the specified language.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# ルートエンドポイント
@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Language Script Executor!"}

# 非同期でスクリプトを実行するエンドポイント
@app.post("/execute/{script_name}")
async def execute_script(script_name: str, script_input: ScriptInput):
    script_path = SCRIPT_DIRECTORY / script_name

    if not script_path.is_file():
        raise HTTPException(status_code=404, detail="Script not found")

    # 実行言語のコマンドを取得
    command = LANGUAGE_COMMANDS.get(script_input.language.lower())
    if not command:
        raise HTTPException(status_code=400, detail="Unsupported language specified")

    # ユーザーから受け取った入力をスクリプトに渡す
    result = await run_script(command, script_path, script_input.input_value)

    return {
        "script_name": script_name,
        "language": script_input.language,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
