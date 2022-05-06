from art import logo, vs
import random
from game_data import data
from replit import clear


def format_data(account): 
  """Format the account data into printable format."""
  
  account_name  = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got """
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

  
# Display art
print(logo)
score = 0
game_sholud_continue = True
account_b = random.choice(data)

# Make the game repeatable.

while game_sholud_continue:
  # Generates a random account form the game
  account_a = account_b
  account_b = random.choice(data) 
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
    
  # Ask user fgor a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct
  a_follower_count= account_a['follower_count']
  b_follower_count = account_b['follower_count']
  ## Get follower count of each account.
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  # Give user feedback on thier guess.
  if is_correct:
    score +=1 
    print(f"You're right Current score : {score}.")
  
  else:
    game_sholud_continue=False
    print("Sorry that's wrong.")


# Clear the screen between rounds.

# Making account at position B become the next account at postion.

