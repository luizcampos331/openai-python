import unittest

def run_tests():
	"""Descobre e executa os testes."""
	unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("tests"))

if __name__ == "__main__":
  run_tests()