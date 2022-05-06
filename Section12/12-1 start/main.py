################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

# print(position_strength)


# Global Scope
player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)
drink_potion()

def game():
  def drink_position():
    potion_strength = 2
    print(player_health)

  drink_potion()
