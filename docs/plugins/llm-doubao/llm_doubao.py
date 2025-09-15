from llm import Model
import httpx

class DoubaoModel(Model):
    model_id = "doubao"
    name = "豆包大模型"
    key_env_var = "LLM_DOUBAO_KEY"
    
    def execute(self, prompt, stream, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.get_key()}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "doubao-pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": kwargs.get("temperature", 0.7)
        }
        
        with httpx.Client() as client:
            response = client.post(
                "https://api.doubao.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=120
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]