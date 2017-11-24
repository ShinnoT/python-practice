import random

health = 50

difficulty = 1

# the more difficult the game, the harder it is for the user to gain health
# this logic is defined by dividing the randomely generated added health by the difficulty

potion_health = int(random.randint(25, 50) / difficulty)

# python you can call mehods by brackets in the begginning like int(), not like ruby at the end .to_i
# float() ==  .to_f as well

health += potion_health
print(health)
