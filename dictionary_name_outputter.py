students = {
  "male":["tom", "charlie", "harry", "frank"],
  "female":["jenna", "sarah", "huda", "samantha", "ellie"]
}

for key in students.keys():
  for name in students[key]:
    print(name)
