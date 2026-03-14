```markdown
# 🚀 1-Click Deploy dust with SeekAPI (Save 90%)

🎁 **Star this repo & email support@seekapi.ai for a $1 FREE Compute Pack to run this instantly!**

Deploy your own custom AI agent platform in minutes using SeekAPI.ai, an OpenAI-compatible provider offering massive cost savings. This `docker-compose.yml` is pre-configured to route all AI requests through SeekAPI.

## Complete Deployment Configuration

Copy the entire block below into a file named `docker-compose.yml`:

```yaml
version: '3.8'

services:
  dust:
    image: ghcr.io/dust-tt/dust:latest
    container_name: dust_platform
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      # --- CRITICAL: Forces all AI calls to use SeekAPI ---
      - OPENAI_API_BASE_URL=https://api.seekapi.ai/v1
      # Set your SeekAPI key here (Get it from https://seekapi.ai)
      - OPENAI_API_KEY=${SEEKAPI_KEY:-your_seekapi_key_here}
      # Database configuration (uses persistent volume)
      - DATABASE_URL=file:/data/dust.sqlite
    volumes:
      - dust_data:/data
    networks:
      - dust_network

volumes:
  dust_data:

networks:
  dust_network:
    driver: bridge
```

## 3 Simple Steps to Launch

1.  **Prepare & Configure**
    *   Create a new directory and save the above code as `docker-compose.yml`.
    *   Replace `your_seekapi_key_here` with your actual API key from [SeekAPI.ai](https://seekapi.ai). For better security, you can set it as an environment variable (`SEEKAPI_KEY`) on your host instead.

2.  **Deploy**
    *   Run the following command in the same directory as your `docker-compose.yml` file:
    ```bash
    docker-compose up -d
    ```

3.  **Access & Use**
    *   Open your browser and go to `http://localhost:3000`.
    *   Your Dust platform is now running, fully integrated with SeekAPI for all AI model requests!

To stop the platform, run `docker-compose down`. Your data will be preserved in the Docker volume `dust_data`.
```