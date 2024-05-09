from typing import Optional
from services.OllamaService import OllamaService
from services.translations.TranslationService import TranslationService


class OllamaTranslationService(TranslationService):
  def __init__(self, client: Optional[OllamaService]=None) -> None:
    self.client = client or OllamaService()

  def translate(self, text: str) -> str:
    system_prompt = """
      I get text to translate, from english to polish or from polish to english depend on content.
      I have to return only tranlsation! I don't add any additional description/ information, just pure translation.
    """

    return self.client.process_request(system_prompt, text)