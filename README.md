# 🚀 SeekAPI: The Global Gateway to DeepSeek R1 & V3

[![GitHub stars](https://img.shields.io/github/stars/yourusername/seekapi-python.svg)](https://github.com/yourusername/seekapi-python/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Stop overpaying for OpenAI. Access the world's most powerful reasoning models at 1/10th the cost.**

[SeekAPI.ai](https://seekapi.ai) provides a high-speed, low-latency bridge for global developers to access DeepSeek models without the hurdles of Chinese phone numbers or payment restrictions.

## 🌟 Why SeekAPI?

| Feature | OpenAI (GPT-4o) | DeepSeek (via SeekAPI) |
| :--- | :--- | :--- |
| **Price per 1M Tokens** | ~$15.00 | **$0.15** |
| **Reasoning (R1)** | Expensive | **Ultra Low Cost** |
| **Compatibility** | Standard | **100% OpenAI Compatible** |
| **Payment** | Credit Card | **Credit Card & Crypto (USDT)** |

## ⚡ Quick Start (30 Seconds)

1. Get your API Key at [SeekAPI.ai](https://seekapi.ai).
2. Change one line of code:

```python
import openai

client = openai.OpenAI(
    api_key="your_seekapi_key", 
    base_url="https://api.seekapi.ai/v1"
)

response = client.chat.completions.create(
    model="deepseek-reasoner", # Use R1
    messages=[{"role": "user", "content": "Solve Riemann Hypothesis"}]
)
print(response.choices[0].message.content)
