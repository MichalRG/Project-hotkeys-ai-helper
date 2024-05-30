from services.AnthropicService import AnthropicService
from services.gramma.GrammaService import GrammaService



class AnthropicGrammaService(GrammaService):
  def __init__(self, client: AnthropicService) -> None:
    self.client = client

  def fix_text(self, question: str) -> str:
    system_prompt = """
      I get a sentence, my task it to check, improve gramma, correct all mistakes and return a transcribed corrected version of the text.
      I have to keep context I cannot add any new information, each data should be covered. 
      I'll return answer in user language I won't add any additional information or intro text, I wont answer any questions I'll just return corrected text.
    """
    question += "\nIt's fixed version of text:"

    return self.client.process_request(system_prompt, question, 1000)