#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

def gg():



  def set_difficulty():
    attempts = 0
    while attempts == 0:
      difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")   
      if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number.")
      elif difficulty == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number.")
      else:
        print("Invalid input! Try again.")
    return attempts
      
    
  print(logo)
  sec_num = random.randint(0, 100)

  print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. \n"
  f"Pssst, the correct answer is {sec_num}")

  no_attempts = set_difficulty()
  print (no_attempts)

  while no_attempts > 0:
    user_guess = int(input("Make a guess: "))
    if user_guess > sec_num:
      no_attempts -= 1
      print(f"Too high! Try again.\n You have {no_attempts} guesses left.")
    elif user_guess < sec_num:
      no_attempts -= 1
      print(f"Too low! Try again.\n You have {no_attempts} guesses left.")
    elif user_guess == sec_num:
      print(f"You got it. The answer was {sec_num}")
      break
  
  if no_attempts == 0:
    print (f"You have run out of guesses, the answer was {sec_num}")

  another_game = input("Do you want to play again? Type y or n.")
  if another_game == "y":
    clear()
    gg()
  else:
    exit()

gg()

