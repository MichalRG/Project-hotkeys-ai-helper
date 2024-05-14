from services.ConfigService import ConfigService
from services.OllamaService import OllamaService
from services.OpenAIService import OpenAIService
from services.generalQuestions.OllamaGeneralQuestionService import OllamaGeneralQuestionService
from services.generalQuestions.OpenAIGeneralQuestionService import OpenAIGeneralQuestionService
from services.translations.DeepLTranslationService import DeepLTranslationService
from services.translations.OllamaTranslationService import OllamaTranslationService
from services.translations.OpenAITranslationService import OpenAITranslationService


class ClientsFactory:
  def __init__(self, **kwargs) -> None:
    self.config = kwargs.get('config', ConfigService().get_config())
    self.open_service = OpenAIService()
    self.ollama_service = OllamaService()

    self.opena_ai_tranlsation_service = OpenAITranslationService(self.open_service)
    self.deepl = DeepLTranslationService()
    self.ollama_ai_translation_service = OllamaTranslationService(self.ollama_service)

    self.open_ai_general_question_service = OpenAIGeneralQuestionService(self.open_service)
    self.ollama_ai_general_question_service = OllamaGeneralQuestionService(self.ollama_service)


  def get_translation_service(self) -> OpenAITranslationService | DeepLTranslationService | OllamaTranslationService:
    transaltion_service = self.config.get('translation', {}).get('engine', '')
    model = self.config.get('translation', {}).get('model')

    if transaltion_service == 'deepl':
      return self.deepl
    elif transaltion_service == 'ollama':
      self.ollama_service.set_model(model)  

      return self.ollama_ai_translation_service
    else:
      self.open_service.set_model(model)

      return self.opena_ai_tranlsation_service
    
  def get_general_question_service(self) -> OpenAIGeneralQuestionService | OllamaGeneralQuestionService:
    general_question_service = self.config.get('general_question', {}).get('engine')
    model = self.config.get('general_question', {}).get('model')

    if general_question_service == 'ollama':
      self.ollama_service.set_model(model)
      return self.ollama_ai_general_question_service
    else:
      self.open_service.set_model(model)
      return self.open_ai_general_question_service
