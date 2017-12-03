known_users = ["alice", "bob", "claire", "dan", "emma", "fred", "george", "harry"]

print(len(known_users)) # will return length of the list

while True:
  print("hi my name is travis your security bot!")
  name = input("Whats your name?: ").strip().lower()

  if name in known_users:
    print("name recognized")
  else:
    print("name NOT recognized")
