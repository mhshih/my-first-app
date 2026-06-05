import google.genai as genai
client = genai.Client(api_key="")

from google.genai import types
response = client.models.generate_content(
            model='gemini-2.5-flash',
                contents=types.Part.from_text(text='翻成日語：今天天氣真好'),
                    config=types.GenerateContentConfig(
                                temperature=0,
                                        top_p=0.95,
                                                top_k=20,
                                                    ),
                    )

# 印出回應
print(response.text)
