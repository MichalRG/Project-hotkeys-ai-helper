from typing import Optional
from services.OpenAIService import OpenAIService
from utils.cliboard import get_clipboard, paste_to_cliboard


class EventManager:
  def __init__(self) -> None:
    self.open_ai_service = OpenAIService()

  def translate_event(self, text:Optional[str]=None):
    system_prompt = """
      I get text to translate, from english to polish or from polish to english depend on content.
      I have to return only tranlsation! I don't add any additional description/ information, just pure translation.
    """
    if not text:
      text = get_clipboard()

    response = self.open_ai_service.process_request(system_prompt, text, token_limit=300)

    paste_to_cliboard(response)