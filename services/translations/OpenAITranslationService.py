from services.OpenAIService import OpenAIService
from services.translations.TranslationService import TranslationService


class OpenAITranslationService(TranslationService):
  def __init__(self, client: OpenAIService) -> None:
    self.client = client or OpenAIService()

  def translate(self, text: str) -> str:
    system_prompt = """
      I get text to translate, from english to polish or from polish to english depend on content.
      I have to return only tranlsation! I don't add any additional description/ information, just pure translation.
    """

    return self.client.process_request(system_prompt, text, token_limit=300)
