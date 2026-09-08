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


@app.get("/api/services")
def get_services():

  # 1. 原始資料 (List + Dictionary)
  services_data = [
      {
          "id": 1,
          "name": "合規與風險控制諮詢",
          "price": 10000,
          "description": "SFC 合規架構搭建與風險評估。",
          "duration": "3 個工作天"
      },
      {
          "id": 2,
          "name": "AML 反洗錢系統評估",
          "price": 15000,
          "description": "評估與部署專業 AML 系統。",
          "duration": "7 個工作天"
      },
      {
          "id": 3,
          "name": "虛擬資產牌照通知服務",
          "price": 20000,
          "description": "虛擬資產交易服務監管申報與業務計劃。",
          "duration": "14 個工作天"
      },
  ]

  # 2. 💡 今日想練習嘅 Python 邏輯：根據金額給予不同折扣 (If-Else)
  for item in services_data:
    original_price = item["price"]

    # 練習 Python If-Else 條件判斷
    if original_price >= 20000:
      discount_rate = 0.8  # 滿 2萬 打 8 折
    elif original_price >= 15000:
      discount_rate = 0.85  # 滿 1.5萬 打 85 折
    else:
      discount_rate = 0.9  # 其他打 9 折

    # 練習新增動態欄位
    item["discount_price"] = int(original_price * discount_rate)
    item["savings"] = original_price - item["discount_price"]  # 算出了省了多少錢


  return {
      "company": "Springfield Consultancy",
      "status": "success",
      "services": services_data,
  }
