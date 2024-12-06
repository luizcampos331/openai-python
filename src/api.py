from openai import OpenAI
from .config import OPENAI_API_KEY

class OpenAIApi:
  def __init__(self):
    self.client = OpenAI(
      api_key=OPENAI_API_KEY
    )

  def get_client(self):
    return self.client