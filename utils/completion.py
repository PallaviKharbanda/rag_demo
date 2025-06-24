import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("EURI_API_KEY")

def generate_completion(prompt, model="gpt-4.1-nano", temperature=0.3):
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": temperature
    }
    try:
        res = requests.post(url, headers=headers, json=payload, verify=False)  # or use certifi
        res.raise_for_status()  # Raises error for 4xx/5xx responses
        data = res.json()

        if "choices" in data:
            return data['choices'][0]['message']['content']
        else:
            return f"⚠️ Unexpected API response: {data}"

    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {str(e)}"
    except Exception as e:
        return f"❌ Something went wrong: {str(e)}"
