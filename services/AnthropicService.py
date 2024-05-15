import os
from typing import Optional

import anthropic


class AnthropicService:
  def __init__(self, model: Optional[str] = "claude-3-haiku-20240307") -> None:
    self.client = anthropic.Anthropic(api_key=os.getenv("APIKEY-ANTHROPIC"))
    self.model = model

  def set_model(self, model:str):
    if not model:
      print("ERROR with setting model lack of model variable")
      return
    
    self.model = model

  def process_request(
    self,
    system_message: str,
    user_prompt: str, 
    token_limit:int = 300,
    model: Optional[str] = None, 
  ) -> str:
    params = {
      "model": model or self.model,
      "system":  system_message,
      "max_tokens": token_limit,
      "messages": [
        {"role": "user", "content": user_prompt}
      ]
    }

    response = self.client.messages.create(
      **params
    )

    return(response.content[0].text)