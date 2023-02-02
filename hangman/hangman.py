import math
from random import choice
from lib import *

class Game:
    def __init__(self):
        self.current_guessed_word = None
        self.incorrect_guess_count = None
        self.guesses = None
        self.secret_word = None
        self.words = filter_words(fetch_words())
        self.max_guesses = None
        self.start_game()
    def play_game(self):
        while True:
            try:
                print(hangman_pics[math.floor(self.incorrect_guess_count / 2)]) # Print the current stage of hangman
            except IndexError: # Out of index range
                print(hangman_pics[6]) # Print last stage

            print(self.current_guessed_word)
            print('You have', self.max_guesses - self.incorrect_guess_count, 'guesses left')
            print("GUESS COUNT:", self.incorrect_guess_count) # Number of incorrect guesses

            guess = input("GUESS: ").lower() # Lowercase guess for verification
            if not verify_input(guess): # Verify guess
                print("Enter one ALPHABETIC character.")
                continue # Ask for input again
            if guess in self.guesses:
                print("You have already GUESSED that.")
                continue # Ask for input again
            guess_occurrences = find_occurrences(self.secret_word, guess) # Find all the indexes of the occurrences of the guess in the secret word
            self.guesses.append(guess)
            if len(guess_occurrences) == 0: # If the guess does not exist in the secret word
                self.incorrect_guess_count = self.incorrect_guess_count + 1
                if self.incorrect_guess_count == self.max_guesses:
                    print("You have LOST.")
                    break # Reset game
            for occurrence in guess_occurrences: # For each index of the guess occurring in the secret word, add to the current guessed word
                self.current_guessed_word = replace_char_in_string(occurrence, self.current_guessed_word, guess)
            if self.current_guessed_word == self.secret_word: # If user has won
                print("You WON WITH", self.incorrect_guess_count, format_win_string(self.incorrect_guess_count))
                break

    def start_game(self):
        stop_playing = False
        while not stop_playing:
            print("H A N G M A N\n", hangman_pics[6]) # Welcome screen
            play_choice = input("Welcome to HANGMAN. Type 'exit' to exit or anything else to play. ")
            if play_choice == 'exit':
                stop_playing = True # Stop playing
            else:
                """INIT ALL VALUES"""
                self.secret_word = choose_secret_word(self.words)
                self.guesses = []
                self.incorrect_guess_count = 0
                self.current_guessed_word = '-' * len(self.secret_word)
                self.max_guesses = find_max_guesses(self.secret_word)
                self.play_game()
