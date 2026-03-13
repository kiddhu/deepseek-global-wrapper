# How to use quivr with SeekAPI (Save 90% on API Costs)

🎁 **BONUS:** Star this repository (kiddhu/deepseek-global-wrapper) and email your GitHub handle to support@seekapi.ai to receive a **$2 Free Compute Pack** instantly!

Integrating powerful Retrieval-Augmented Generation (RAG) into your applications just got significantly more affordable. By combining the flexible, open-source **quivr** project with **SeekAPI's OpenAI-compatible endpoint**, you can build sophisticated AI features while cutting your LLM API costs by up to 90%.

This guide shows you the exact configuration needed to point quivr to SeekAPI.

## Prerequisites

*   A SeekAPI account and an API key. [Sign up here](https://seekapi.ai).
*   A running instance of quivr. [Follow the official quivr setup guide](https://github.com/StanGirard/quivr).

## Configuration: Connect quivr to SeekAPI

The key is to configure quivr's environment variables to use SeekAPI as its LLM provider.

### 1. Locate Your quivr `.env` File

Navigate to the root directory of your quivr installation. You should find a `.env` file (or a `.env.example` you can copy).

### 2. Set the OpenAI-Compatible Variables

Edit the `.env` file and add or update the following variables. This tells quivr to send all its LLM requests to SeekAPI instead of the official OpenAI API.

```bash
# SeekAPI Configuration
OPENAI_API_KEY=sk-your-seekapi-key
OPENAI_API_BASE=https://api.seekapi.ai/v1

# Optional: Specify a specific model available on SeekAPI
# OPENAI_API_MODEL=deepseek-chat
```

**Explanation:**
*   `OPENAI_API_KEY`: Replace `sk-your-seekapi-key` with your **actual SeekAPI key**.
*   `OPENAI_API_BASE`: This **must be set exactly to `https://api.seekapi.ai/v1`**. This is the SeekAPI endpoint that quivr will call.
*   `OPENAI_API_MODEL`: (Optional) You can lock quivr to use a specific, cost-effective model from SeekAPI's catalog (e.g., `deepseek-chat`, `qwen-plus`). If not set, quivr will use the model name it requests internally (like `gpt-4`), which SeekAPI will route to a compatible, affordable model.

### 3. Restart Your quivr Services

For the changes to take effect, restart your quivr application. The method depends on your setup (e.g., Docker):

```bash
docker-compose down
docker-compose up -d
```

## You're Ready!

That's it. Your quivr instance is now powered by SeekAPI. All interactions—brain management, document ingestion, Q&A—will use SeekAPI's low-cost, high-performance models.

### Verification & Cost Savings

1.  **Test a Query:** Go to your quivr web interface and ask a question based on your uploaded documents. It should work seamlessly.
2.  **Check Your SeekAPI Dashboard:** Log into your [SeekAPI dashboard](https://seekapi.ai/dashboard) to monitor usage. You'll see the requests from quivr and the significantly lower cost per call compared to standard OpenAI prices.

## Customization Tips

*   **Model Selection:** Experiment with different `OPENAI_API_MODEL` values in your `.env` file to find the best balance of performance, speed, and cost for your use case directly from the SeekAPI model list.
*   **Vector Stores & Files:** Remember, quivr handles the RAG pipeline—your document processing, vector storage (PGVector, FAISS), and retrieval logic remain unchanged and fully under your control. SeekAPI simply provides the affordable LLM for the final generation step.

By making this simple switch, you maintain all the powerful customization and data control of quivr while leveraging SeekAPI to make it economically sustainable.