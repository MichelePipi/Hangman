from random import choice
from lib import *

class Game:
    def __init__(self):
        words = filter_words(fetch_words())
        self.guess_count = 0
        self.secret_word = choice(words)
        self.current_word = '-' * len(self.secret_word)
        self.guesses = []
        self.start_game()
    def play_game(self):
        while True:
            print(hangman_pics[self.guess_count])
            print("GUESS COUNT:", self.guess_count)
            guess = input("GUESS: ")
            if guess in self.guesses:
                print("You have already GUESSED that.")
                continue
            if not verify_input(guess):
                print("Enter one ALPHABETIC character.")
                continue
            guess_occurrences = find_occurrences(self.secret_word, guess)
            if len(guess_occurrences) == 0:
                self.guess_count = self.guess_count + 1
                if self.guess_count > 6:
                    print("You have LOST.")
                    break
            for occurrence in guess_occurrences:
                self.current_word = replace_char_in_string(occurrence, self.current_word, guess)
            if self.current_word == self.secret_word:
                print("You WON in", self.guess_count, 'GUESS(ES).')
                break

    def start_game(self):
        stop_playing = False
        while not stop_playing:
            print("H A N G M A N\n", hangman_pics[6])
            play_choice = input("Welcome to HANGMAN. Type 'exit' to exit or anything else to play. ")
            if play_choice == 'exit':
                stop_playing = True # Stop playing
            else:
                self.play_game()
