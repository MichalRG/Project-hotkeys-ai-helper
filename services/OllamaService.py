from typing import Optional
import ollama

class OllamaService:
  def __init__(self, model: str="Mistral") -> None:
    self.ollama_model_name = model

  def set_model(self, model: str):
    self.ollama_model_name = model

  def process_request(
    self,
    system_message: str,
    user_prompt: str, 
    model: Optional[str] = None, 
  ) -> str:
    response = ollama.chat(model= model or self.ollama_model_name, messages=[
      {
        'role': 'user',
        'content': user_prompt,
      }, {
        'role': 'system',
        'content': system_message or ''
      }
    ])
    
    return response['message']['content']
 