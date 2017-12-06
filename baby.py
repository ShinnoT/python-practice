from random import choice


questions = ["why is the sky blue", "how does the internet work", "where are dinasours"]
question = choice(questions)
answer = input("{}?: ".format(question)).strip().lower()

while answer != "just because":
  answer = input("why?: ").strip().lower()
