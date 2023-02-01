from lib import *


class Game:
    def __init__(self):
        self.words = filter_words(fetch_words())
    def debug(self):
        print(self.words)
