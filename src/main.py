from src.chat import OpenAIChat
import unittest

def main():
  print("OpenAI CLI Chat - Type 'exit' to quit.")

  chat = OpenAIChat()
  messages = []

  while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
      print("\nExiting. Goodbye!")
      break

    messages.append({"role": "user", "content": user_input})
    response = chat.get_response(messages)
    messages.append({"role": "assistant", "content": response})
    print(f"\nOpenAI: {response}")

def run_tests():
  unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("tests"))

if __name__ == "__main__":
  main()