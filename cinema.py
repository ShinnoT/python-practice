films = {
  "annabelle":[3,2],
  "casino royale":[18,5],
  "motorcycle diaries":[15,5]
}

while True:
  choice = input("what film would you like to watch?: ").strip()

  if choice in films:
    age = input("how old are you?: ").strip()
    if (int(age) >= films[choice][0]) and (films[choice][1] > 0):
      print("enjoy film")
      films[choice][1]-=1
    elif (int(age) >= films[choice][0]) and (films[choice][1] <= 0):
      print("no more seats left")
    else:
      print("too young for film")
  else:
    print("we dont have that film")
