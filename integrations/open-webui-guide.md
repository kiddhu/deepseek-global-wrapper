# How to use open-webui with SeekAPI (Save 90% on API Costs)

🎁 **BONUS:** Star this repository (kiddhu/deepseek-global-wrapper) and email your GitHub handle to support@seekapi.ai to receive a **$2 Free Compute Pack** instantly!

[open-webui](https://github.com/open-webui/open-webui) is a fantastic open-source UI that lets you interact with various AI models. By connecting it to SeekAPI's OpenAI-compatible endpoint, you can access powerful models like DeepSeek, Llama, and Qwen at a fraction of the cost of leading providers.

Here’s how to set it up in under 2 minutes.

## Step 1: Deploy or Access Your open-webui Instance
If you haven't already, follow the [official open-webui installation guide](https://docs.openwebui.com/getting-started/installation/). You can run it via Docker, Kubernetes, or use their cloud version.

## Step 2: Add SeekAPI as a Connection
1.  Open your open-webui interface.
2.  Click on your profile picture/icon in the top-right corner and select **"Settings"**.
3.  Navigate to the **"Connections"** tab in the settings menu.
4.  Click the **"Add New Connection"** button.

## Step 3: Configure the Connection
Fill in the connection form with the following SeekAPI details:

*   **Connection Name:** `SeekAPI` (or any name you prefer)
*   **API Base URL:** `https://api.seekapi.ai/v1`
*   **API Key:** `sk-your-seekapi-key` (Replace this with your [actual SeekAPI key](https://seekapi.ai))
*   **Provider:** Select **`OpenAI`** from the dropdown list.

**Important:** Ensure the **"Model Discovery"** option is **ENABLED**. This allows open-webui to automatically fetch the list of available models from SeekAPI.

## Step 4: Save and Select Models
1.  Click **"Save"** to add the connection.
2.  Go to the main chat interface.
3.  Click on the model selector (usually near the top of the chat window). You should now see all available SeekAPI models (e.g., `deepseek-chat`, `llama-3.1-8b-instruct`, `qwen2.5-7b-instruct`) listed under your new connection.
4.  Select your desired model and start chatting!

## Example Configuration Summary
| Setting | Value to Use |
| :--- | :--- |
| **Connection Name** | `SeekAPI` |
| **API Base URL** | `https://api.seekapi.ai/v1` |
| **API Key** | Your actual key from [seekapi.ai](https://seekapi.ai) |
| **Provider** | `OpenAI` |

## Troubleshooting
*   **Models not showing?** Double-check that "Model Discovery" is enabled for the connection in Settings > Connections.
*   **API Error?** Verify your API Key is correct and has sufficient credits in your [SeekAPI account](https://seekapi.ai).
*   **Slow responses?** You can switch between different models to find the optimal balance of speed and capability for your task.

You're all set! You now have a sleek, private ChatGPT-like interface powered by SeekAPI's cost-efficient models. Enjoy your savings!