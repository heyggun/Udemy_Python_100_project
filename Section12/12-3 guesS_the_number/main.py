#Include an ASCII art logo.
from random import randint
from art import logo
print(logo)

#Number Guessing Game Objectives:

EASY_LELVEL_TURNS = 10
HARD_LELVEL_TURNS = 5


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level =='easy':
    turns = EASY_LELVEL_TURNS

  else:
    turns = HARD_LELVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\nPsst, the correct answer is 100")
  game_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  answer = randint(1,101,1)
  
  # Allow the player to submit a guess for a number between 1 and 100.
  turns = set_difficulty()
  print(f'You have {turns} attempts remaining to guess the number.')
  

  guess = 0 
  # If they run out of turns, provide feedback to the player. 
  while guess !=answer:
    guess = int(input('Make a guess:'))

    if guess > answer:
      print('Too high.')
  
    elif guess < answer:
      print('Too low.')
  
    else:
      print(f'You got it! The answer was {answer}')

    
  
game()



# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


