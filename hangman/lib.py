import requests, re, sys


def fetch_words() -> list:
    """Fetches the 1000 most popular US English words from a URL"""
    print("Fetching words list...", end='')
    url = 'https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt'
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
    return [word for word in words if 4 <= len(word) <= 9]


def find_occurrences(secret_word, guess) -> list:
    """
    Finds the occurrences of the guess in the secret word and outputs a list of indexes where the guess is found.
    """
    return [i for i in range(len(secret_word)) if guess == secret_word[i]]


def verify_input(guess: str) -> bool:
    return len(guess) != 1 or not bool(re.match('[a-z]', guess.lower()))


def replace_char_in_string(index, string, replace) -> str:
    listed_string = list(string)
    listed_string[index] = replace
    return "".join(listed_string)


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