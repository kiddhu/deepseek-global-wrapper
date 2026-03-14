```markdown
# 🚀 1-Click Deploy cultivation-world-simulator with SeekAPI (Save 90%)

🎁 **Star this repo & email support@seekapi.ai for a $1 FREE Compute Pack to run this instantly!**

Deploy the open-source AI-powered Cultivation World Simulator in minutes using SeekAPI.ai, an OpenAI-compatible API provider offering massive savings. This `docker-compose.yml` is pre-configured to route all AI requests through SeekAPI.

## Complete Deployment Configuration

Copy the following `docker-compose.yml` to your server:

```yaml
version: '3.8'

services:
  cultivation-world-simulator:
    image: ghcr.io/opencultivation/cultivation-world-simulator:latest
    container_name: cultivation-world-simulator
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      # Force all OpenAI API calls to use SeekAPI's endpoint
      - OPENAI_API_BASE_URL=https://api.seekapi.ai/v1
      # Replace with your actual SeekAPI key from https://seekapi.ai
      - OPENAI_API_KEY=${SEEKAPI_KEY:-your_seekapi_key_here}
      # Project-specific environment variables (adjust as needed)
      - NODE_ENV=production
      - PORT=3000
    volumes:
      # Persist simulation data and agent memories
      - ./data:/app/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

## 3 Simple Steps to Run

1.  **Get Your API Key:** Sign up at [seekapi.ai](https://seekapi.ai) and get your API key. Replace `your_seekapi_key_here` in the `docker-compose.yml` file with your real key, or set it as an environment variable (`export SEEKAPI_KEY=sk-yourkey`).

2.  **Launch the Simulator:** In the directory containing your `docker-compose.yml` file, run:
    ```bash
    docker-compose up -d
    ```

3.  **Access the World:** Open your browser and navigate to `http://your-server-ip:3000`. The cultivation world simulator is now running, powered by SeekAPI!

To stop the simulator, run `docker-compose down`. Your simulation data will be preserved in the `./data` directory.
```