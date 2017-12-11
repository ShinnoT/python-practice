import random

class Coin:
  def __init__(self, rare=False, clean=True, heads=True, **kwargs):

    for key,value in kwargs.items():
      setattr(self,key,value)
      #set attributes will do self.original_value = 1.00 etc. automatically


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

  def clean():
      self.color = self.clean_color

  def __del__(self):
    print("coin spent")

  def flip(self):
    heads_options = [True,False]
    choice = random.choice(heads_options)
    self.heads = choice


# generate a Pound class that inherits from parent class Coin
class Pound(Coin):
  def __init__(self):
    data = {
      "original_value":1.00,
      "clean_color":"gold",
      "rusty_color":"greenish",
      "diameter":22.5,
      "mass":9.5
    }
    super().__init__(**data) #unpack data and make new parent class instance


# generated a one_pence class
class One_Pence(Coin):
  def __init__(self):
    data = {
      "original_value":0.01,
      "clean_color":"bronze",
      "rusty_color":"brownish",
      "diameter":20.3,
      "mass":3.56
    }
  super().__init__(**data)


#generated a two_pence class
class Two_Pence(Coin):
  def __init__(self):
    data = {
      "original_value":0.02,
      "clean_color":"bronze",
      "rusty_color":"brownish",
      "diameter":25.9,
      "mass":7.12
    }
  super().__init__(**data)

  #polymorphism --> overriding parent instance methods inside children
  def rust(self):
    self.color = self.clean_color

  #this is unnecessary cuz not really overriding but for demonstration purposes
  def clean(self):
    self.color = self.clean_color
