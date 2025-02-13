from fastapi import FastAPI, HTTPException
import subprocess
import asyncio
from pathlib import Path

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# スクリプトが保存されているディレクトリ（絶対パスで指定）
SCRIPT_DIRECTORY = Path(__file__).parent / "api" / "scripts"

# 非同期でスクリプトを実行する関数
async def run_script(script_path: Path):
    try:
        # サンドボックス内で非同期にスクリプトを実行
        result = await asyncio.to_thread(subprocess.run, 
                                          ["python", str(script_path)], 
                                          text=True, capture_output=True, timeout=10)
        return result
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Script execution timed out")
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Script execution failed with error: {e.stderr}")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Python executable not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# ルートエンドポイント
@app.get("/")
async def root():
    return {"message": "Welcome to CodeStoradge-Executions!"}

# 非同期でスクリプトを実行するエンドポイント
@app.post("/execute/{script_name}")
async def execute_script(script_name: str):
    # スクリプトの絶対パスを構築
    script_path = SCRIPT_DIRECTORY / script_name

    # スクリプトが存在するか確認
    if not script_path.is_file():
        raise HTTPException(status_code=404, detail="Script not found")

    # 非同期実行
    result = await run_script(script_path)

    # 結果をJSONレスポンスとして返す
    return {
        "script_name": script_name,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
