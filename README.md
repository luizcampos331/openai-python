<h1 align="center">
  OpenAI CLI Chat
</h1>

## Index
<p align="center">
  <a href="#bookmark-about">About</a> |
  <a href="#computer-technologies-used">Technologies</a> |
  <a href="#dart-objective">Objective</a> |
  <a href="#gear-requirements">Requirements</a> |
  <a href="#package-how-to-download-the-project">Download</a> |
  <a href="#wrench-how-to-use">How to Use</a> |
  <a href="#bust_in_silhouette-author">Author</a> |
  <a href="#pencil-license">License</a>
</p>

## :bookmark: About
OpenAI CLI Chat is a Python-based command-line interface (CLI) application designed to interact with the OpenAI API.

This project serves as an example of how to integrate OpenAI’s services into Python applications while following best practices like object-oriented programming and modular project organization.

## :computer: Technologies Used

- Python 3.8+
- OpenAI API
- python-dotenv
- unittest (for testing)

## :dart: Objective

The main objectives of this project are:
- Demonstrate how to call the OpenAI API to generate responses based on user prompts.
- Build a simple yet functional command-line interface.
- Showcase how to structure a Python project with clean architecture and object-oriented programming.

## :gear: Requirements

- Python 3.8 or higher: Download from python.org.
- OpenAI API Key: Get your API key from OpenAI.
- A code editor (we recommend Visual Studio Code).

## :package: How to Download the Project

Open your terminal, navigate to your desired folder, and run the commands below:

```
  # Clone the repository
  $ git clone https://github.com/luizcampos331/openai-python.git

  # Navigate to the project directory
  $ cd openai-python

  # Create a virtual environment and activate it
  $ python -m venv .venv
  $ source .venv/bin/activate # On Linux/MacOS
  # or
  $ source .venv\Scripts\activate # On Windows

  # Install the project as a package
  $ pip install -e .
```

## :wrench: How to Use

1. Duplicate the file .env.example, rename to .env and define your "OPENAI_API_KEY":
```
OPENAI_API_KEY=your-api-key-here
```

2. Run the application:
```
start-chat
```

3. Type your messages in the terminal to interact with the API. To exit, type exit.

## Running Tests

To execute unit tests:
```
run-tests
```

## :bust_in_silhouette: Author

Luiz Eduardo Campos da Silva
LinkedIn: @luiz-campos
GitHub: @luizcampos331

## :pencil: License

Copyright © 2020 <a href="https://www.github.com/luizcampos331">Luiz Campos</a></br>
This project is licensed under the <a href="LICENSE">MIT license</a>.