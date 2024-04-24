from abc import ABC, abstractmethod


class TranslationService(ABC):
  @abstractmethod
  def translate(self, text:str) -> str:
    pass