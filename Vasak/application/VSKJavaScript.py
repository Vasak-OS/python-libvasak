import os

class VSKJavaScript:
  def __init__(self, page):
    self.page = page
  
  def send(self, script: str) -> None:
    """
    * Send custom JavaScript
    """
    try:
      self.page.runJavaScript(f"{self._is_file_or_string(script)}")
    except Exception as err:
      print(err)
  
  def _is_file_or_string(self, script: str) -> str:
    if os.path.exists(script) and os.path.isfile(script):
      try:
        with open(script, "r") as file:
          string = file.read()
          return string
      except Exception as err:
        print(err)
    elif isinstance(script, str):
      return script