known_users = ["alice", "bob", "claire", "dan", "emma", "fred", "george", "harry"]

print(len(known_users)) # will return length of the list

while True:
  print("hi my name is travis your security bot!")
  name = input("Whats your name?: ").strip().lower()

  if name in known_users:
    print("name recognized! hello {}".format(name))
    remove = input("would you like to be removed from the system (y/n)?: ").strip().lower()

    if remove == "y":
      known_users.remove(name) #only deletes the first instance of name so if name occurs twice it wont work on the second one
      #if you want to remove an element from the list using an index then do
      #del known_users[0]
      #OR del known_users[0:3]
      #OR del known_users[0::2]
      print("you are removed!")
    else:
      print("cool thanks for using the app")

  else:
    print("name NOT recognized")
    add = input("would you live to be added (y/n)?: ").strip().lower()

    if add == "y":

