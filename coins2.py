import random

class Coin:
  def __init__(self, rare=False, clean=True, heads=True):
    self.is_rare = rare
    self.is_clean = clean
    self.heads = heads

    if self.is_rare:
      self.value = self.original_value * 1.25 #value of coin increases 25% if it is rare
    else:
      self.value = self.original_value

    if self.is_clean:
      self.color = self.clean_color
    else:
      self.color = self.rusty_color

  def rust(self):
      self.color = self.rusty_color

  def clear():
      self.color = self.clean_color

  def __del__(self):
    print("coin spent")

  def flip(self):
    heads_options = [True,False]
    choice = random.choice(heads_options)
    self.heads = choice
