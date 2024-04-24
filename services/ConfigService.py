import json

class ConfigService:
  def get_config(self) -> dict:
    with open('./config.json', 'r') as file:
      data = json.load(file)
    return data
