import httpx
import os

class SeekAPI:
    """SeekAPI.ai 官方 Python SDK - 跨境算力套利核心引擎"""
    def __init__(self, api_key=None, base_url="https://dash.seekapi.ai/v1"):
        self.api_key = api_key or os.getenv("SEEKAPI_API_KEY")
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, model, messages, stream=False):
        """调用推理算力 (支持 DeepSeek R1/V3)"""
        payload = {"model": model, "messages": messages, "stream": stream}
        with httpx.Client(timeout=60.0) as client:
            response = client.post(f"{self.base_url}/chat/completions", json=payload, headers=self.headers)
            return response.json()

    def get_balance(self):
        """查询账户实时余额"""
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/user/quota", headers=self.headers)
            return response.json()
