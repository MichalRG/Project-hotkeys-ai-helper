from typing import Optional
from services.OllamaService import OllamaService
from services.gramma.GrammaService import GrammaService



class OllamaGrammaService(GrammaService):
  def __init__(self, client: Optional[OllamaService] = None) -> None:
    self.client = client or OllamaService()

  def fix_text(self, question: str) -> str:
    system_prompt = """
      I get a sentence, my task it to check, improve gramma, correct all mistakes and return a transcribed corrected version of the text.
      I have to keep context I cannot add any new information, each data should be covered. 
      I'll return answer in user language I won't add any additional information, I wont answer any questions I'll jsut return corrected text.
    """

    return self.client.process_request(system_prompt, question)