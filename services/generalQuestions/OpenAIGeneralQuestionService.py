from services.OpenAIService import OpenAIService
from services.generalQuestions.GeneralQuestionService import GeneralQuestionService


class OpenAIGeneralQuestionService(GeneralQuestionService):
  def __init__(self, client: OpenAIService) -> None:
    self.client = client or OpenAIService()

  def answer_question(self, question: str) -> str:
    system_prompt = """
      I get a question to answer, based on my general knowledge I have to answer in most clear and efficient way.
      My explanation should be brief and short as possible. I won't add any additional text and description, just pure answer.
    """

    return self.client.process_request(system_prompt, question)