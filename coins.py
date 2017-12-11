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