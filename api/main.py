from fastapi import FastAPI

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# ルートエンドポイント
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
