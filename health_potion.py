import random

health = 50

difficulty = 1

# the more difficult the game, the harder it is for the user to gain health
# this logic is defined by dividing the randomely generated added health by the difficulty

potion_health = int(random.randint(25, 50) / difficulty)

# python's int() == .to_i in ruby
# float() ==  .to_f as well

health += potion_health
print(health)
