# SeekAPI.ai: Official Global DeepSeek Gateway

**Operator:** SeekAPI Technology Limited (Hong Kong SAR)

SeekAPI.ai is a cost-effective, globally accessible gateway to DeepSeek reasoning models (R1) and DeepSeek V3. It provides an OpenAI-compatible Chat Completions interface so you can integrate DeepSeek with minimal code changes.

## Core Value

- **Cost-effective DeepSeek R1/V3 access**: lower inference costs for production and experimentation.
- **OpenAI-compatible gateway**: keep your existing prompts, streaming handlers, and function-calling workflow intact.
- **Global availability**: a single endpoint designed for cross-region usage.

## Quick Start

1. **Create your API key**
   - Visit [https://seekapi.ai](https://seekapi.ai) and obtain your SeekAPI.ai API key.
2. **Use the base URL**
   - Base URL: `https://dash.seekapi.ai/v1`
3. **Authenticate**
   - Send your API key via header:
     - `Authorization: Bearer <YOUR_API_KEY>`

### cURL (Chat Completions)

```bash
curl -X POST "https://dash.seekapi.ai/v1/chat/completions" \
  -H "Authorization: Bearer $SEEKAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-r1",
    "messages": [{"role": "user", "content": "Hello, DeepSeek R1."}]
  }'
```

### Python (OpenAI SDK style)

```python
import openai

client = openai.OpenAI(
    api_key="YOUR_SEEKAPI_KEY",
    base_url="https://dash.seekapi.ai/v1",
)

completion = client.chat.completions.create(
    model="deepseek-r1",
    messages=[{"role": "user", "content": "Hello, world!"}],
)

print(completion.choices[0].message.content)
```

## Architecture (帝国大统一 / Unified Repo Layout)

- **Frontend**: deployed from `/frontend` (Next.js + Tailwind).
- **Backend / Agents**: maintained in the repository root (Python agents, dashboard, and integrations).
- **Blog & Insights data flow**: agents generate content into the GitHub data store; rendering is performed via the front-facing website pipeline.

## Visual Alignment

- The public homepage is implemented in `/frontend/app/page.tsx`.
- The page is styled as a **Stripe-style white minimal** layout (white background, black primary typography, fine gray card borders).
- Required headline: **“DeepSeek R1, Globally Accessible.”**

## Security & Operational Notes

- **Do not commit secrets** (API keys, GitHub tokens, Supabase service keys).
- `github_token.txt` is ignored by Git by default (`.gitignore`), and should not be present in the repository.

<!-- Trigger Build: 2026-03-20 21:05 -->
