import pyperclip


def get_clipboard() -> str:
  return pyperclip.paste()

def paste_to_cliboard(text: str):
  pyperclip.copy(text)
