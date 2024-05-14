import os
from typing import Optional
from openai import OpenAI
import openai


class OpenAIService:
  def __init__(self, model: Optional[str] = "gpt-3.5-turbo") -> None:
    self.client = OpenAI(api_key=os.getenv("APIKEY-OPENAI"))
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
    model: Optional[str] = None, 
    token_limit:Optional[int] = None
  ) -> str:
    params = {
      "model": model or self.model,
      "messages": [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt}
      ]
    }
    if (token_limit):
      params["max_tokens"]=token_limit

    response = self.client.chat.completions.create(
      **params
    )

    return(response.choices[0].message.content.strip())