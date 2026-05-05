"""
Quick test for RunPod LLM endpoint
"""
import requests
import time

# Your configuration
LLM_ENDPOINT_ID = "XX"
API_KEY = "XX"



def test_llm():
    url = f"https://api.runpod.ai/v2/{LLM_ENDPOINT_ID}/runsync"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "input": {
            "prompt": "Hello World"
        }
    }
    
    print("🚀 Testing LLM endpoint...")
    print(f"Endpoint: {LLM_ENDPOINT_ID}")
    print(f"Request: {payload}\n")
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ SUCCESS! Response:")
            print("-" * 60)
            print(result)
            print("-" * 60)
        else:
            print(f"\n❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.Timeout:
        print("⏱️ Request timed out - endpoint might still be initializing")
        print("Wait a few minutes and try again")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_llm()