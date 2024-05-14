from typing import Optional
from services.OllamaService import OllamaService
from services.generalQuestions.GeneralQuestionService import GeneralQuestionService


class OllamaGeneralQuestionService(GeneralQuestionService):
  def __init__(self, client: Optional[OllamaService] = None) -> None:
    self.client = client or OllamaService()

  def answer_question(self, question: str) -> str:
    system_prompt = """
      I get a question to answer, based on my general knowledge I have to answer in most clear and efficient way.
      My explanation should be brief and short as possible. I won't add any additional text and description, just pure answer.
    """

    return self.client.process_request(system_prompt, question)