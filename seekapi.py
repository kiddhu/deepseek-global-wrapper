import openai

class SeekAPI:
    """
    SeekAPI.ai: The Global Bridge to DeepSeek R1 & V3.
    95% cheaper than OpenAI. 100% compatible.
    """
    def __init__(self, api_key, base_url="https://api.seekapi.ai/v1"):
        # This allows developers to use SeekAPI as a drop-in replacement for OpenAI
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def chat(self, prompt, model="deepseek-chat", stream=True):
        """
        Simple wrapper for chat completions.
        Models: 'deepseek-chat' (V3) or 'deepseek-reasoner' (R1)
        """
        return self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=stream
        )

# Quick Test Example:
# if __name__ == "__main__":
#     client = SeekAPI(api_key="your_sk_here")
#     response = client.chat("Hello, SeekAPI!")
#     print(response)
