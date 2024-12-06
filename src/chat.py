from src.api import OpenAIApi
from .config import (
  OPENAI_MODEL,
  OPENAI_TEMPERATURE,
  OPENAI_MAX_TOKENS
)

class OpenAIChat:
  def __init__(self):
    self.client = OpenAIApi().get_client()

  def get_response(self, messages):
    return self.client.chat.completions.create(
      model=OPENAI_MODEL,
      messages=messages,
      temperature=OPENAI_TEMPERATURE,
      max_tokens=OPENAI_MAX_TOKENS,
    ).choices[0].message.content