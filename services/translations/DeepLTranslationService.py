from services.DeepLService import DeepLService
from services.translations.TranslationService import TranslationService


class DeepLTranslationService(TranslationService):
  def __init__(self) -> None:
    self.client = DeepLService()

  def translate(self, text:str) -> str:
    return self.client.translate(text)