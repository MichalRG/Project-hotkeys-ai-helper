from services.OpenAIService import OpenAIService
from services.translations.DeepLTranslationService import DeepLTranslationService
from services.translations.OpenAITranslationService import OpenAITranslationService


class ClientsFactory:
  def __init__(self) -> None:
    self.open_ai_service = OpenAIService()
    self.opena_ai_tranlsation_service = OpenAITranslationService(self.open_ai_service)
    self.deepl = DeepLTranslationService()

  def get_translation_service(self, config) -> OpenAITranslationService | DeepLTranslationService:
    transaltion_service = config.get('translation', {}).get('engine', '')

    if transaltion_service == 'deepl':
      return self.deepl
    else:
      return self.opena_ai_tranlsation_service