from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允許你的 GitHub Pages 讀取資料 (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
  return {"message": "Render Python API 運作正常！"}


# 💡 練習：寫一個回傳 Consultancy 服務列表與計算折扣的 API
@app.get("/api/services")
def get_services():
  # 練習：Python 字典 (Dictionary) 與 清單 (List)
  services_data = [
      {"id": 1, "name": "合規與風險控制諮詢", "price": 10000},
      {"id": 2, "name": "AML 系統評估與部署", "price": 15000},
      {"id": 3, "name": "虛擬資產牌照通知服務", "price": 20000},
  ]

  # 練習：Python 邏輯計算（例如全部服務打 9 折）
  discount_rate = 0.9
  for item in services_data:
    item["discount_price"] = int(item["price"] * discount_rate)

  return {
      "company": "Springfield Consultancy",
      "status": "success",
      "services": services_data,
  }
