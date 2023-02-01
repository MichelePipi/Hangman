import requests
from Hangman import Game


def fetch_words() -> list:
    """Fetches the 1000 most popular US English words from a URL"""
    url = 'https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt'
    response = requests.get(url)
    return [word for word in response.text.splitlines()]


def filter_words(words: list) -> list:
    """Filter words based on length"""
    return [word for word in words if 4 <= len(word) <= 9]


def run_hangman() -> None:
    game = Game()
    game()


if __name__ == '__main__':
    run_hangman()
