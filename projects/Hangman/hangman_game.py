from pathlib import Path
import utils
import random
from dataclasses import dataclass
from player_manager import PlayerManager
import time

class HangMan:
    
    def __init__(self):
        self.lives = 6

    def choose_random_word(self, words_list: list) -> str:

        random_word = random.choice(words_list)
        return random_word

    def game_round(self, round_type: utils.RoundType):

        self.lives = 6
        if round_type == utils.RoundType.EASY:
            increment_score = 5
            words_list = utils.easy_words
        elif round_type == utils.RoundType.MEDIUM:
            increment_score = 10
            words_list = utils.medium_words
        elif round_type == utils.RoundType.HARD:
            increment_score = 15
            words_list = utils.hard_words
        elif round_type == utils.RoundType.BONUS:
            increment_score = 25
            words_list = utils.tech_words
        else:
            increment_score = 0

        word = self.choose_random_word(words_list)
        n_letters = len(word)

        word_sliced = []
        ambiguous_word_display = []
        for letters in word:
            word_sliced.append(letters)
            ambiguous_word_display.append("_")

        wrong_guesses = 0
        correct_guesses = 0

        while True:

            if self.lives == 0:
                print(f"You lost! Your word was {word}.")
                print("Status: ", utils.player_status[wrong_guesses])
                print(utils.HANGMAN_PICS[wrong_guesses], "\n")
                increment_score = 0
                return increment_score
            
            if correct_guesses == n_letters:
                print("🎉 Congratulations! You guessed the word!")
                print(f"You've been awarded {increment_score} points.\n")
                return increment_score

            print("Your word:", ambiguous_word_display)
            print("Status: ", utils.player_status[wrong_guesses])
            print(utils.HANGMAN_PICS[wrong_guesses], "\n")

            user_guess = utils.get_valid_input(str, "Your guess: ")
            user_guess = user_guess.strip().lower()

            if len(user_guess) == 1:
                if user_guess in word_sliced:
                    print("✅ Correct Guess!")
                    
                    for i, letter in enumerate(word_sliced):
                        if user_guess == letter and ambiguous_word_display[i] == "_":
                            ambiguous_word_display[i] = letter
                            correct_guesses += 1
                    
                else:
                    print("❌ Incorrect Guess!")
                    self.lives -= 1
                    wrong_guesses += 1
                

            elif len(user_guess) == n_letters:
                if user_guess == word:
                    correct_guesses = n_letters
                    continue

                else:
                    print("❌ Incorrect Guess!")
                    self.lives = self.lives - 1
                    wrong_guesses = wrong_guesses + 1

            else:
                print("Guess one letter at a time!")
                continue

