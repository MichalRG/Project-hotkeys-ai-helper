from abc import ABC, abstractmethod


class GrammaService(ABC):
  @abstractmethod
  def fix_text(self, text: str) -> str:
    pass