import requests
import random
from flask import Flask, jsonify, request

API_URL = 'https://wordle.votee.dev:8000'

app = Flask(__name__)
WORDLE_API_URL = 'https://wordle.votee.dev:8000/random'
WORD_LIST = ["apple", "banjo", "crane", "drive", "eagle"]
WORD_LIST_Random = ["ppale", "jonba", "anecr", "ivedr", "gleea"]


def fetch_random_word(seed):
    random_idx=random.randint(0,4)

    return WORD_LIST_Random[random_idx],WORD_LIST[random_idx]

def compare_words(targeted_word, guessed_word):
    feedback=[]
    for i in range(len(targeted_word)):
        if guessed_word[i]==targeted_word[i]:
            feedback.append("correct")
        elif guessed_word[i] in targeted_word:
            feedback.append('present')
        else:
            feedback.append('absent')
    return feedback


def guess_random_word(seed):
    random_word,actual_word = fetch_random_word(seed)
    if random_word:
        print(f"Random word generated: {random_word}")
        print(f"actual word generated: {actual_word}")
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        max_attempts = 1000
        attempts = 0
        guess = 'a'*len(random_word)

        while attempts < max_attempts:
            feedback=compare_words(actual_word,guess)
            print(f"Guess: {guess}, Feedback: {feedback}")

            if all(fb== 'correct' for fb in feedback):
                print("Word guessed correctly!")
                return guess
                break
            else:
                guess = refine_guess(guess, feedback, random_word)
                attempts += 1


        if attempts >= max_attempts:
            print("Max attempts reached. Failed to guess the word.")


def refine_guess(current_guess, feedback, target_word):
    new_guess = list(current_guess)

    for i,fb in enumerate(feedback):
        if fb=='absent':
            new_guess[i] = next_letter(current_guess[i])
        elif fb=='present':
            new_guess[i] = next_letter(current_guess[i])
        else:
            new_guess[i]=new_guess[i]
    print(new_guess)
    return ''.join(new_guess)


def next_letter(char):
    return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))


@app.route('/guess_word', methods=['GET'])
def guess_word_endpoint():
    seed = request.args.get('seed', default=1234, type=int)
    guessed_word = guess_random_word((seed))
    if guessed_word:
        return jsonify({"guessed_word": guessed_word})
    else:
        return jsonify({"error": "Failed to guess word"}), 500


if __name__ == '__main__':
    app.run(debug=True)
