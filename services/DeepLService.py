import os
import deepl


class DeepLService:
  def __init__(self) -> None:
    self.client = deepl.Translator(os.getenv('APIKEY-DEEPL', ''))

  def translate(self, data: str) -> str:
    translation = self.client.translate_text(data, target_lang="PL")

    if translation.detected_source_lang == 'EN':
      return translation.text 
    
    return self.client.translate_text(data, target_lang="EN-US").text 


