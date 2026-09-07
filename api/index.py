from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    # 設定回傳狀態碼 200 (成功)
    self.send_response(200)

    # 設定跨域 (CORS) 標頭，允許 GitHub Pages 網頁呼叫這個 API
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    # 準備要回傳給前端網頁的資料
    response_data = {
        'status': 'success',
        'company': 'Springfield',
        'message': 'Hello! 這是在 Vercel 運行的 Python API！',
    }

    # 轉換成 JSON 格式並輸出
    self.wfile.write(json.dumps(response_data).encode('utf-8'))
    return
