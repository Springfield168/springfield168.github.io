from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 設定跨域 (CORS)，允許你嘅 GitHub Pages 網頁連過來讀取資料
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def get_api_data():
  return {
      "status": "success",
      "company": "Springfield",
      "message": "Hello! 這是在 Render 運行的 Python API！",
  }
