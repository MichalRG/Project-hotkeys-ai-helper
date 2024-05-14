from typing import Optional
from services.ConfigService import ConfigService
from services.WolframAlphaService import WolframAlphaService
from services.factories.ClientsFactory import ClientsFactory
from utils.cliboard import get_clipboard, paste_to_cliboard


class EventManager:
  def __init__(self) -> None:
    self.config = ConfigService().get_config()
    clients_factory = ClientsFactory(config=self.config)
    self.translation_service = clients_factory.get_translation_service()
    self.general_question_service = clients_factory.get_general_question_service()
    self.wolfram_service = WolframAlphaService()

  def translate_event(self, text:Optional[str]=None):
    if not text:
      text = get_clipboard() 

    response = self.translation_service.translate(text)
    
    paste_to_cliboard(response)

  def process_wolfram_action(self, text:Optional[str]=None):
    if not text:
      text = get_clipboard() 
    
    response = self.wolfram_service.make_wolfram_question(text)
    
    paste_to_cliboard(response)

  def process_general_question(self, text:Optional[str]=None):
    if not text:
      text = get_clipboard()

    response = self.general_question_service.answer_question(text)

    paste_to_cliboard(response) 