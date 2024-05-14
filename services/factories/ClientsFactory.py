from services.ConfigService import ConfigService
from services.OpenAIService import OpenAIService
from services.translations.DeepLTranslationService import DeepLTranslationService
from services.translations.OllamaTranslationService import OllamaTranslationService
from services.translations.OpenAITranslationService import OpenAITranslationService


class ClientsFactory:
  def __init__(self, **kwargs) -> None:
    self.config = kwargs.get('config', ConfigService().get_config())
    self.open_ai_service = OpenAIService()
    self.opena_ai_tranlsation_service = OpenAITranslationService(self.open_ai_service)
    self.deepl = DeepLTranslationService()
    self.ollama_ai_translation_service = OllamaTranslationService()

  def get_translation_service(self) -> OpenAITranslationService | DeepLTranslationService | OllamaTranslationService:
    transaltion_service = self.config.get('translation', {}).get('engine', '')

    if transaltion_service == 'deepl':
      return self.deepl
    elif transaltion_service == 'ollama':
      return self.ollama_ai_translation_service
    else:
      open_ai_model = self.config.get('translation', {}).get('model', 'gpt-4o')
      self.open_ai_service.set_model(open_ai_model)

      return self.opena_ai_tranlsation_service