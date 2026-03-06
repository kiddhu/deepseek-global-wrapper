# 🚀 SeekAPI: The Global Gateway to DeepSeek R1 & V3

[![GitHub stars](https://img.shields.io/github/stars/kiddhu/deepseek-global-wrapper.svg?style=social)](https://github.com/kiddhu/deepseek-global-wrapper/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Website](https://img.shields.io/badge/Website-seekapi.ai-indigo)](https://seekapi.ai)

**Stop overpaying for OpenAI. Access the world's most powerful reasoning models at 1/10th the cost.**

[SeekAPI.ai](https://seekapi.ai) provides a high-speed, low-latency bridge for international developers to access **DeepSeek R1 & V3** without the hurdles of Chinese phone numbers or payment restrictions.

---

## 🎁 Star for $1.00 Free Credit!
1. **Star** this repository ⭐
2. Register at [SeekAPI.ai](https://seekapi.ai)
3. Email your GitHub ID to `support@seekapi.ai` to claim your **$1.00 credit**.

---

## 🌟 Why SeekAPI?

| Feature | OpenAI (GPT-4o) | DeepSeek (via SeekAPI) |
| :--- | :--- | :--- |
| **Price per 1M Tokens** | ~$15.00 | **$0.15** (99% Savings) |
| **Reasoning (R1)** | Expensive | **Ultra Low Cost** |
| **Compatibility** | Standard | **100% OpenAI Compatible** |
| **Payment** | Credit Card Only | **Credit Card & Crypto (USDT)** |
| **Access** | Global | **Global (No VPN Required)** |

## ⚡ Quick Start (Python)

SeekAPI is a drop-in replacement for OpenAI. Just change the `base_url`:

```python
import openai

client = openai.OpenAI(
    api_key="your_seekapi_key", 
    base_url="https://api.seekapi.ai/v1"
)

response = client.chat.completions.create(
    model="deepseek-reasoner", # This is DeepSeek R1
    messages=[{"role": "user", "content": "Explain Quantum Entanglement in 3 sentences."}]
)

print(response.choices[0].message.content)
