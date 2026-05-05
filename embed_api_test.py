import requests

EMBEDDING_ENDPOINT_ID = "XX"
API_KEY = "XX"

def get_embeddings(texts):
    url = f"https://api.runpod.ai/v2/{EMBEDDING_ENDPOINT_ID}/runsync"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": {
            "model": "BAAI/bge-small-en-v1.5",
            "input": texts  # Can be a string or list of strings
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["output"]["data"]

# Use it
embeddings = get_embeddings("What is machine learning?")
print(embeddings)