import requests, re, sys, random


def fetch_words() -> list:
    """Fetches the 1000 most popular US English words from a URL"""
    print("Fetching words list...", end='')
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt'
    try:
        response = requests.get(url) # Try to grab words list
    except requests.exceptions.RequestException: # Error retrieving words list [wifi error most likely]
        print(' ❌')
        print("A SEVERE exception occurred while trying to retrieve the words dictionary. \nPlease check your internet connection.")
        sys.exit(-1)
    print(' ✅')
    return [word for word in response.text.splitlines()] # Return words list by creating a list looping through each word in a string created by response.text.splitlines()


def filter_words(words: list) -> list:
    """Filter words based on length"""
    return [word for word in words if 4 <= len(word) <= 5] # For each word in words list, remove every occurrence <4 len or >5 len


def find_occurrences(secret_word: str, guess: str) -> list:
    """Finds the occurrences of the guess in the secret word and outputs a list of indexes where the guess is found."""
    return [i for i in range(len(secret_word)) if guess == secret_word[i]]


def verify_input(guess: str) -> bool:
    """Checks if the input is valid as a guess"""
    return len(guess) == 1 and bool(re.match('[a-z]', guess))


def replace_char_in_string(index: int, string: str, replace: str) -> str:
    listed_string = list(string) # Convert string into a list
    listed_string[index] = replace # Replace the char in the string
    return "".join(listed_string) # Convert the list back into a string


def format_win_string(count: int) -> str:
    """Formats the string for the event of winning a game for plurals."""
    if count > 2 or count == 0: # Plural or 0
        return 'INCORRECT GUESSES'
    return 'INCORRECT GUESS'


def choose_secret_word(words: list) -> str:
    return random.choice(words)


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
