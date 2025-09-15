from llm import Model
import httpx

class KimiModel(Model):
    model_id = "kimi"
    name = "Kimi智能助手"
    key_env_var = "LLM_KIMI_KEY"

    def execute(self, prompt, stream, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.get_key()}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "kimi-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": kwargs.get("temperature", 0.3)
        }
        
        with httpx.Client() as client:
            response = client.post(
                "https://api.moonshot.cn/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=120
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]