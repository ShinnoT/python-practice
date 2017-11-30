#get user email address

email = input("What is your email address?: ").strip()

#slice out user name

username = email[:email.index("@")]

#slice domain name

#here if we start at "@" it will include that "@" so..
domain = email[email.index("@") + 1 :]

#format message
output = "Your username is {} and your domain name is {}".format(username, domain)

#display output message
print(output)
