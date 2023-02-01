import requests, re, sys


def fetch_words() -> list:
    """Fetches the 1000 most popular US English words from a URL"""
    print("Fetching words list...", end='')
    url = 'https://ftp.michelepip.xyz/Hangman/static/words_list.txt'
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print(' ❌')
        print("A SEVERE exception occurred while trying to retrieve the words dictionary. \nPlease check your internet connection.")
        sys.exit(-1)
    print(' ✅')
    return [word for word in response.text.splitlines()]


def filter_words(words: list) -> list:
    """Filter words based on length"""
    return [word for word in words if 4 <= len(word) <= 7]


def find_occurrences(secret_word, guess) -> list:
    """
    Finds the occurrences of the guess in the secret word and outputs a list of indexes where the guess is found.
    """
    return [i for i in range(len(secret_word)) if guess == secret_word[i]]


def verify_input(guess: str) -> bool:
    return len(guess) == 1 and bool(re.match('[a-z]', guess))


def replace_char_in_string(index, string, replace) -> str:
    listed_string = list(string)
    listed_string[index] = replace
    return "".join(listed_string)


def format_guesses(count: int) -> str:
    if count > 2 or count == 0:
        return 'INCORRECT GUESSES'
    return 'INCORRECT GUESS'


hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']