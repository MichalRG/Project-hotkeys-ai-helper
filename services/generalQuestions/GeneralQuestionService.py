from abc import ABC, abstractmethod


class GeneralQuestionService(ABC):
  @abstractmethod
  def answer_question(self, text: str) -> str:
    pass