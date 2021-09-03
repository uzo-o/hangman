"""
name: hangman.py
author: Uzo Ukekwe
version: python 3.8
purpose: plays games of hangman keeping track of wins/losses
"""

import sys
import random
import time

word = ""             # the word to be guessed
characters = []       # the characters of the word to be guessed
answers = []          # the letters the user has guessed so far
letter = False        # letter guessed (False when none exists)
strikes = 5           # number of guesses left
wins = 0
losses = 0
round_done = False


def clear_screen():
    """
    Clear the screen before next guess
    """
    print("\n" * 50)


def display_man():
    """
    Print the hangman structure after every guess
    """
    global strikes

    print('     ------')
    print('     |    |')

    # num of strikes determine if part of body will be visible
    if strikes < 5:
        print('     |    ┌─┐\n     |    ┴─┴  ')
    else:
        print('     |     ')
    if strikes < 4:
        print('     |   (^-^)')
    else:
        print('     |     ')
    if strikes < 3:
        print('     |   /   \\')
    else:
        print('     |     ')
    if strikes < 2:
        print('     |     |')
    else:
        print('     |     ')
    if strikes < 1:
        print('     |   /   \\')
    else:
        print('     |     ')

    print("   ---------")


def reminders():
    """
    Tell the player relevant info about the current state of their game
    """
    global strikes
    global answers
    global letter
    global wins
    global losses

    print(f'You have {strikes} strikes remaining.')
    print(f'The current word is: {answers}')

    # decreases wait time if you've entered letters or finished a game before
    if letter or wins + losses > 0:
        time.sleep(2)
    else:
        time.sleep(5)


def user_entry():
    """
    Accept a letter from the user and print the outcome
    """
    global strikes
    global answers
    global letter
    global characters

    good_guess = False

    letter = input("Guess a letter (or the full word): ").lower().strip()
    while letter in answers:
        letter = input("You already guessed that letter.\nGuess a new letter: ").lower().strip()

    i = 0
    if len(letter) > 1:
        if letter == word:
            answers = list(letter)
        else:
            print("That was not the word :(")
            strikes -= 1
    else:
        while i < len(characters):
            if letter == characters[i]:
                print("You guessed a correct letter!")
                answers[i] = letter
                good_guess = True
            else:
                if i == len(characters) - 1:
                    if not good_guess:
                        print("You didn't guess a correct letter :(")
                        strikes -= 1
            i += 1


def check_win_or_loss():
    """
    Tell the user if they have won or lost the current game
    """
    global answers
    global characters
    global strikes
    global wins
    global losses
    global word
    global round_done

    if answers == characters:
        wins += 1
        print(f"The word was {word}!\nYou Win!")
        print(f'You have {wins} win(s) and {losses} loss(es).')
        round_done = True
        print()
    elif strikes == 0:
        losses += 1
        print(f"The word was {word}, you loser!")
        print(f'You have {wins} win(s) and {losses} loss(es).')
        round_done = True
        print()


def play_game(dictionary):
    """
    Play one game from start to finish
    :param dictionary: words available to be guessed
    """
    global letter
    global round_done
    global word
    global strikes
    global characters
    global answers

    display_man()
    check_win_or_loss()

    if not round_done:
        reminders()
        clear_screen()
        user_entry()
        letter = True       # user has begun entering letters

    if round_done:
        outcome = input("a) play again\nb) exit\n").lower().strip()
        outcomes = ["a", "b"]
        while outcome not in outcomes:
            outcome = input("a) play again\nb) exit\n").lower().strip()
        if outcome == "a":
            clear_screen()
            word = dictionary[random.randint(0, len(dictionary) - 1)]
            strikes = 5
            characters = list(word)
            answers = []
            for i in characters:
                answers.append("_")
            letter = False
            round_done = False
        elif outcome == "b":
            sys.exit()


def main():
    """
    Run hangman games until the user exits
    """
    global word
    global characters
    global answers
    # global letter

    # choose word to guess during first game
    dictionary = ["frog", "cat", "aardvark", "bear", "lion"]
    word = dictionary[random.randint(0, len(dictionary) - 1)]

    # populate guessing blanks
    characters = list(word)
    answers = []
    for i in characters:
        answers.append("_")

    print("     HANGMAN")

    while True:
        play_game(dictionary)


if __name__ == "__main__":
    main()
