import google.generativeai as genai
from google.colab import userdata

# 從 Colab secret 讀取 API key（不要寫死在 cell 裡！）
genai.configure(api_key=userdata.get("GEMINI_API_KEY"))

# 選一個模型
model = genai.GenerativeModel("gemini-2.5-flash")

# 發送請求
response = model.generate_content("翻成日語：今天天氣真好")

# 印出回應
print(response.text)
