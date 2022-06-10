from colored import fg
import random
import time
import sys
colory = fg('yellow')
colorw = fg('white')
colorb = fg('blue')
colorr = fg('red')
colorg = fg('green')
colorc = fg('cyan')
colorb = fg('blue')

wordList = ["accident",
  "appendicitis",
  "assailant",
  "accuse",
  "accustom",
  "articulate",
  "arrange",
  "asymmetrical",
  "automobile",
  "active"]

# TODO - HOMEWORK: adding the welcome message and let user know the game rules here
def log(text,delay):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(delay)
str = colory + "Welcome to Hangman! 😃\n" + colorw + "HOW TO PLAY: Input one letter at a time and try to guess the word with a certain number of guesses!\n"
log(str,0.1)

# TODO: STEP 1: get a random index by using random.randint()
ranIndex = random.randint(0,len(wordList)-1)
# get the word by using the random index that we got above
word = wordList[ranIndex]
word = word.upper()
# print(word)

# TODO: STEP 2: create a set of all unique characters in the word
uniqueLetters = set(word)
# print(uniqueLetters)

# create a variable to store the hangman lives
life = len(word) + 3
if life > 1:
  print (colorg + f"You have {life} lives!")
else:
  print (colorr + f"You have {life} life!")

# TODO: create an empty set that will store all the user guesses (e.g.: already_guessed_letters = set())
userGuesses = set()

while life > 0 and len(uniqueLetters) > 0:
  
  # let the user know which characters they already chose
  if len(userGuesses) > 0:
    print(colorc + f"Here is the list of all the letters that you have chosen: {userGuesses}")

  # show the order of the letter in the word
  colorm = fg('magenta')
  print(colorm + "The word is", end=" ")
  for eachLetter in word:
    if eachLetter in userGuesses:
      print(eachLetter, end=" ")
    else:
      print("_", end=" ")
  print()
  
  # TODO: get the user input
  # get the guessing letter from the user
  guess = input(colorw + "\nWhat is your guess: ")
  guess = guess.upper()
  print(f"You entered {guess}.")
  
  # check if the user already guessed the letter before, then let them know
  if guess in userGuesses:
    print(colorb + "You already picked that letter before. 🤨")
  # if the user input a number of invalid input, let them know
  elif not guess.isalpha():
    print(colorb + "That is not a letter. 🧐")
  # if the user input a letter that hasn't picked before and it's a valid input
  else:
    # if the guess is correct
    if guess in word:
      print(colory + "Your letter is in the word! 😁")
      uniqueLetters.remove(guess) # remove the user input from the uniqueLetters
      userGuesses.add(guess) # add the user guess character into the userGuesses)
    # if the guess is incorrect
    else: 
      print(colorb + "Your letter is not in the word. 😭")
      life -= 1
      userGuesses.add(guess) # add the user guess character into the userGuesses)

  # show how many lives user has left
  if life > 1:
    print(colorg + f"You have {life} lives left.")
  else:
    print(colorr + f"You have {life} life left.")

# let users know if they win the game
if len(uniqueLetters) > 0:
  print(colorr + "\nSorry! You failed to guess the word. 😞")
else:
  print(colorg + "\nHooray! You guessed the word! 🤗")
  
# let the user know the word at the end
print(colorc + f"This is the secret word: {word} 🤫")