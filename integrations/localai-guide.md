# How to use LocalAI with SeekAPI (Save 90% on API Costs)

🎁 **BONUS:** Star this repository (kiddhu/deepseek-global-wrapper) and email your GitHub handle to support@seekapi.ai to receive a **$2 Free Compute Pack** instantly!

## Why LocalAI + SeekAPI?

Running powerful AI models locally with [LocalAI](https://github.com/mudler/LocalAI) gives you privacy and control. But what if you need to access your self-hosted models from anywhere, or share them with your team? That's where SeekAPI comes in.

SeekAPI provides a production-ready, OpenAI-compatible endpoint for your LocalAI instance, allowing you to:
- Access your local models from any application
- Use standard OpenAI SDKs and libraries
- Scale beyond your local network
- Pay only for compute, not for expensive API subscriptions

## Quick Start: Connect LocalAI to SeekAPI in 3 Steps

### Step 1: Install and Run LocalAI

```bash
# Using Docker (easiest method)
docker run -p 8080:8080 localai/localai:latest

# Download a model (example: TinyLlama)
curl http://localhost:8080/models/apply -H "Content-Type: application/json" -d '{
  "id": "model-gallery@tinyllama-1.1b"
}'
```

Your LocalAI is now running at `http://localhost:8080` with OpenAI-compatible endpoints.

### Step 2: Connect to SeekAPI

SeekAPI acts as a secure gateway to your LocalAI instance. Use these credentials:

- **Base URL:** `https://api.seekapi.ai/v1`
- **API Key:** `sk-your-seekapi-key` (replace with your actual key from [SeekAPI Dashboard](https://seekapi.ai))

### Step 3: Make Your First API Call

```python
from openai import OpenAI

# Point to SeekAPI, which proxies to your LocalAI
client = OpenAI(
    base_url="https://api.seekapi.ai/v1",
    api_key="sk-your-seekapi-key"  # Your SeekAPI key
)

# Use it just like OpenAI API!
response = client.chat.completions.create(
    model="tinyllama-1.1b",  # Your LocalAI model name
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

## Complete Integration Example

Here's a full Python script that demonstrates the complete workflow:

```python
import openai
import os

# Configuration
OPENAI_API_BASE = "https://api.seekapi.ai/v1"
OPENAI_API_KEY = "sk-your-seekapi-key"  # Get from https://seekapi.ai
LOCALAI_MODEL = "tinyllama-1.1b"  # Your LocalAI model name

# Initialize client
client = openai.OpenAI(
    base_url=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY
)

def chat_with_localai(prompt, model=LOCALAI_MODEL):
    """Send a prompt to your LocalAI via SeekAPI"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    result = chat_with_localai("Write a short poem about open source AI.")
    print(result)
```

## Advanced: Using Different LocalAI Features

### Image Generation (Stable Diffusion)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.seekapi.ai/v1",
    api_key="sk-your-seekapi-key"
)

# Generate an image
response = client.images.generate(
    model="stablediffusion",  # Your LocalAI image model
    prompt="A cute cat programmer coding at a laptop",
    n=1,
    size="512x512"
)

print(f"Image URL: {response.data[0].url}")
```

### Audio Transcription

```python
# Transcribe audio file
with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper",  # Whisper model in LocalAI
        file=audio_file
    )
print(transcript.text)
```

## Cost Comparison: LocalAI+SeekAPI vs. Commercial APIs

| Service | Cost per 1M tokens | Privacy | Custom Models |
|---------|-------------------|---------|---------------|
| OpenAI GPT-4 | ~$30 | ❌ No | ❌ No |
| Anthropic Claude | ~$15 | ❌ No | ❌ No |
| **LocalAI + SeekAPI** | **~$3** | ✅ Yes | ✅ Yes |

**Savings:** Approximately 90% compared to commercial APIs!

## Troubleshooting

### Common Issues & Solutions

1. **"Model not found" error**
   - Check your LocalAI has the model loaded: `curl http://localhost:8080/models`
   - Use exact model name from LocalAI in your API calls

2. **Connection timeout**
   - Ensure your LocalAI instance is running: `docker ps`
   - Check SeekAPI dashboard for connection status

3. **Authentication errors**
   - Verify your API key at [SeekAPI Dashboard](https://seekapi.ai)
   - Ensure key is properly formatted: `sk-...`

## Next Steps

1. **Get your free compute:** Email your GitHub handle to support@seekapi.ai after starring [kiddhu/deepseek-global-wrapper](https://github.com/kiddhu/deepseek-global-wrapper)

2. **Explore more models:** Add different models to LocalAI:
   ```bash
   # Add Llama 2
   curl http://localhost:8080/models/apply -d '{"id": "model-gallery@llama-2-7b"}'
   
   # Add Mistral
   curl http://localhost:8080/models/apply -d '{"id": "model-gallery@mistral-7b"}'
   ```

3. **Monitor usage:** Check your SeekAPI dashboard for usage analytics and billing

## Resources

- [LocalAI Documentation](https://localai.io/)
- [SeekAPI Getting Started](https://docs.seekapi.ai)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference) (compatible with SeekAPI)

---

**Ready to save 90% on AI API costs?** Start by [getting your SeekAPI key](https://seekapi.ai) and connecting your LocalAI instance today!