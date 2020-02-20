import sys
import random
import time

def clearScreen():
  print("\n"*50)

#prints the dude after every guess
def displayMan():
  global strikes
  print('     ------')
  print('     |    |')
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

#tells the player relevant info
def reminders(answers):
  global strikes
  global letter
  global wins
  global losses
  print(f'You have {strikes} strikes remaining.')
  print(f'The current word is: {answers}')
  if letter != 0 or wins+losses > 0:
    time.sleep(2)
  else:
    time.sleep(5)

#accepts letter and prints outcome
def userEntry(letter,characters):
  goodGuess = False
  global strikes
  global answers
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
        goodGuess = True
      else:
        if i == len(characters)-1:
          if goodGuess == False:
            print("You didn't guess a correct letter :(")
            strikes -= 1
      i += 1

#checks if they won or lost so far
def checkWinOrLoss(answers,characters,word,strikes):
  global wins
  global losses
  global done
  if answers == characters:
    wins += 1
    print(f"The word was {word}!\nYou Win!")
    print(f'You have {wins} win(s) and {losses} loss(es).')
    done = True
    print()
  elif strikes == 0:
    losses += 1
    print(f"The word was {word}, you loser!")
    print(f'You have {wins} win(s) and {losses} loss(es).')
    done = True
    print()

#chooses word
dictionary = ["frog","cat","aardvark","bear","lion"]
word = dictionary[random.randint(0,len(dictionary)-1)]

strikes = 5
characters = list(word)
answers = []
for i in characters:
  answers.append("_")
letter = '0'

wins = 0
losses = 0

done = False

print("     HANGMAN")

while True:
  displayMan()
  checkWinOrLoss(answers,characters,word,strikes)
  #mechanism skips the rest of the game functions when the current game ends
  if done == False:
    reminders(answers)
    clearScreen()
    userEntry(letter,characters)
  if done == True:
    outcome = input("a) play again\nb) exit\n").lower().strip()
    outcomes = ["a","b"]
    while outcome not in outcomes:
      outcome = input("a) play again\nb) exit\n").lower().strip()
    if outcome == "a":
      clearScreen()
      word = dictionary[random.randint(0,len(dictionary)-1)]
      strikes = 5
      characters = list(word)
      answers = []
      for i in characters:
        answers.append("_")
      letter = '0'
      done = False
    elif outcome == "b":
      sys.exit()