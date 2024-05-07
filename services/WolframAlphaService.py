import os
import pyperclip
import requests
import xml.etree.ElementTree as ET
import urllib.parse


class WolframAlphaService:
  def __init__(self) -> None:
    self.token = os.getenv('APIKEY-WOLFRAM-ALPHA', '')

  def make_wolfram_question(self, text_to_process: str) -> str:   
    encoded_input = urllib.parse.urlencode({"input": text_to_process})

    url = f'http://api.wolframalpha.com/v2/query?appid={self.token}&{encoded_input}&includepodid=Result&format=plaintext'

    xml_result = requests.get(url).text

    root = ET.fromstring(xml_result)

    result_tag = root.find(".//plaintext")

    if result_tag is not None:
      return result_tag.text or "Wolfram result not found in XML or unavailable"
    else:
      return "Wolfram result not found in XML or unavailable"