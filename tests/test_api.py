import unittest
from unittest.mock import MagicMock, patch
from src.chat import OpenAIChat

class TestOpenAIChat(unittest.TestCase):
  @patch("src.api.OpenAIApi.get_client")
  def test_get_response(self, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.chat.completions.create.return_value = MagicMock(
      choices=[MagicMock(message=MagicMock(content="I'm fine, thank you!"))]
    )

    chat = OpenAIChat()
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    response = chat.get_response(messages)

    self.assertEqual(response, "I'm fine, thank you!")

    mock_client.chat.completions.create.assert_called_once_with(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=0.7,
      max_tokens=150,
    )

if __name__ == "__main__":
  unittest.main()