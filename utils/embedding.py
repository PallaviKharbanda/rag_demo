import requests
import numpy as np
import os
import certifi
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("EURI_API_KEY")  # Use env var for security

def get_embedding(text, model="text-embedding-3-small"):
    url = "https://api.euron.one/api/v1/euri/alpha/embeddings"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"input": text, "model": model}
    #response = requests.post(url, headers=headers, json=payload)
   
    response = requests.post(url, headers=headers, json=payload, verify=False)
    return np.array(response.json()['data'][0]['embedding'])
