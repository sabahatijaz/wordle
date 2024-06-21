# Flask Wordle API

This Project contains a Flask API that fetches a random word from predefined list, makes a guess using the  Wordle-like API, and returns the result.
the wordle_solver api has the code to simply call the Wordle api endpoint
the wordle_api.py has the code that takes a random word from list and makes the guess and 
the custom_word_guess has the code to implement the api that takes a random word and corrects it by making guesses and comparing it with the actual word.
## Requirements

-- Python 3
-- `Flask` Library
-- `requests` Library

## Installation
clone git repos
cd wordle
pip install -r requirements.txt

## Usage
Run the flask app using the command `python wordle_api.py`