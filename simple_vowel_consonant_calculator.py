vowels = 0
consonants = 0
user_input = input("please type a sentence or a word without punctuation: ").strip().lower()

for letter in user_input:
  if letter.lower() in "aeiou":
    vowels += 1
  elif letter == " ":
    pass #pass statement does nothing particular but can act as a placeholder
  else:
    consonants += 1


print("there are {} vowels".format(vowels))
print("there are {} consonants".format(consonants))
