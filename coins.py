import random

class Pound:

  value = 1.00
  color = "gold"
  num_edges = 1
  diameter = 22.5 #milimeters
  thickness = 3.15 #milimeters
  heads = True


coin1 = Pound() #new instance of Pound class
#we can access attributes like this:
coin1.color # will return "gold"

coin2 = Pound()
#changing attributes of instances
coin2.color = "red"
coin2.color # will now return "red"
#but default color for all Poun instances still remain "gold"

coin3 = Pound()
coin3.color # will still return "gold"



class Pound:

  #init method creates new instance of class object
  def __init__(self, rare=False):
    self.rare = rare

    if self.rare:
      self.value = 5.00
    else:
      self.value = 1.00

    self.color = "gold"
    self.diameter = 22.5
    self.heads = True


  #del method deletes new instance of class object (destructive method)
  #useful in this case because we can imitate "spending" a Pound
  def __del__(self):
    print("coin spent")


  def rust(self):
    self.color = "greenish"

  def clean(self):
    self.color = "gold"

  def flip_coin(self):
    heads_options = [True, False]
    choice = random.choice(heads_options) #need to import random at top to use random.choice method
    self.heads = choice


#making a Pund nstance
coin4 = Pound(rare=True)
coin5 = Pound()
coin4.value #will return 5.00
coin5.value #will return 1.00


#using an instance method defined in Pound class
#in order to rust an instance of a coin
coin6 = Pound()
coin6.rust()
coin6.color #will return "greenish"

#doing opposite, so cleaning an instance of Pound
coin6.clean()
coin6.color #will return "gold"

#flipping coin using instance method defined above
coin6.flip_coin()


del coin6
#will return "coin spent" and then will delete the instance
