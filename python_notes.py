round(2.1)
#  >> 2
# this is a built in function
# but since pythons math functions are not that powerful, we import the math module

import math

# now we can use more powerful math functions (methods in ruby)

math.floor(1.5)
# will return 1 because rounds down

math.ceil(2.1)
# will return 3 because rounds up

# we can also do triganometry
math.sin(math.pi / 2)
#returns 1.0

math.cos(0)
# returns 1.0

math.floor(math.sin(math.pi))
# returns 0

math.asin(0)
# returns 0.0

# finding hypotenuse through pythegorian theorem c^2 = a^2 + b^2
# same thing as c = square root of a^2 + b^2
# hypot(a, b)
math.hypot(3, 4)
# will return 5.0


# to calculate exponents
# for example 2^3 then
math.pow(2, 3)
#returns 8.0
# or as a shortcut we can do
2 ** 3
#but this returns 8 as an integer


# to calculate e^9
math.exp(2)

# natural logs
math.log(math.e)
math.log10(1000)
math.log2(8)



# -----------------------------------------------
# STRINGS

"hello"
name = "shinno"

# to use double quotes as a string, u have to use single quotes
message = 'He told me "SHUT UP SHINNO!"'
# or
# to use single quotes as string, you have to use double quotes
message2 = "That's not right shinno"

# to encapsulate multiple line strings use triple single or triple double quotes
romeo = '''Oh juliet
how wonderful you look
roses are red
violets are blue
blah blah'''














# -------------------------------------------------------------------------------
#string methods
#note that strings are immutable meaning they cannot be changed unless
#you redefine the variable
#x = x.upper()

x = "happy birthday"

len(x) #reutrns length of string
x.count("a") # reutrns 2
# note that the count methods always must take at least one argument

x.upper() #upcase in ruby
x.lower() #downcase in ruby
x.capitalize() # returns "Happy birthday"
x.title() # returns "Happy Birthday"


x.isalpha() # returns false because there is a space between happy and birthday which means its not all alphabets
x.isdigit() # returns false because they are not all numbers
x.isalnum() # returns false because they are not only number and letters (there is still a space)

x.index("birthday") # returns 6 because thats when the string "birthday starts"
# note that it start counting from 0
x.index("afaejfbsrjhrg") # returns an error
x.index("BIRTHDAY") # returns error cuz case sensitive

x.find("birthday") # returns 6
x.find("flushrflivusvhrsp") # returns -1
x.find("BIRTHDAY") # returns -1


y = "000hello000"
y.strip() #gets rid of all the spaces, not inbetween spaces tho i think??
y.strip("0") # returns "hello"
y.lstript() # reutrns "hello000"
y.rstrip() # returns "000hello"



#string slicing
word = "hello"
word[0] # returns "h"
word[-1] # returns "o"

#variable[start:end:step]
word = "hellowhatsup"
word[0:5:1] #returns "hello"
#note here that the end value is the one AFTER the one you want
word[5:] #returns "whatsup"
word[:5] #returns "hello"
word[5::2] #reuturns "wasp"

word[::-1] #reverses entire string because it says from start to finish increment -1
#thus returns "pustahwolleh"



#utilizing the index function so that we dont have to count
word[word.index("hello"):word.index("whatsup"):1]
#must note however index only returns the FIRST instance of its argument
#so "helloemo".index("e") will only return 1 because it only looks for that first instance of "e"




#-----------------------------------------------------------------
#booleans
True
False

#booleans are capital in python unlike in ruby


#----conditionals

num1 = 100
num2 = 50

if num1 > num2:
  print("num1 is bigger than num2")
elif num2 > num1:
  print("num2 is bigger than num1")
else:
  print("both numbers are equal")

#will return "num1 is bigger than num2"



#not

not True #returns False
not False #returns True

not 3 > 1 #returns False


#and same as && in ruby
if True and True:
  print("it worked")
# will return "it worked"


#or same as || in ruby
if False or True:
  print("it worked")
#will reutrn "it worked"



#lists in python == array in ruby
our_list = [1, 2, 3, 4, 5, 6]
two = our_list[1]

#list[start:end:step]
#end here signifies "up to but not including"
our_list[0:3:1] #will return [1, 2, 3]


#list within lists
new_list = [[1, 2], [3, 4]]
two = new_list[0][1]
#can also do things like new_list[1][0:1:1]


# append elements to list
my_list = [True, False, True]
my_list = my_list + 1 #wont work
my_list = my_list + [1] # will return [True, False, True, 1]
  #same as doing my_list.append(1)
my_list = my_list + ["BCD"] #will return [True, False, True, "BCD"]
my_list = my_list + list("BCD") #will return [True, False, True, "BCD", "B", "C", "D"]
#list method will only work for strings and other iterable types NOT integers because they are not iterable

#if you want to add an entire list as an element to an existing list
my_list = my_list + [[1, 2, 3]] #will return [True, False, True, [1, 2, 3]]

# my_list.insert(index, value)
my_list.insert(2, 60)
my_list.insert(1, [1, 2, 3])

#HOWEVER note that you cannot do this
my_list = my_list.insert(2, 60)
my_list = my_list.append(1)
#because it will make the variable my_list nil which will return an error
#insert and append and remove methods are suppose to not be assigned variables





# Tuple --> cannot be changed once made
our_tuple = (1, 2, 3)
our_tuple[0] = 100 #will not allow you to do this because tuples are immutable

#you can convert lists into tuples
A = [1, 2, 3]
A = tuple(A) #will return (1, 2, 3)


# cool nifty tricks with lists and tuples
(A,B,C) = 1,2,3
#will return:
#A=1
#B=2
#C=3

D,E,F = [1,2,3]
# will return :
# D=1
# E=2
# F=3

G,H,I = "789"
# will return :
# G='7'
# H='8'
# I='9'




#dictionaries same as hashes in ruby
dictionary = {"shinno":21, "aimi":25}
dictionary["shinno"] # will return 21
dictionary["toshiki"] = 27 #will add "toshiki":27 to dictionary
dictionary["aimi"] = 22 #will change the value of key"aimi" to 22

#deleting key value pair in dictionaries
del dictionary["shinno"] #will delete "shinno" key value pair

#accessing all the keys in dictionaries
dictionary.keys()

#accessing all the values in dictioinaries
dictionary.values()

#accessing all keys and values through index
a = list(dictionary.keys())
#then you can do a[0]
b = list(dictionary.values())
#then you can do b[0]

#you can also do
list(dictionary.keys())[2:]

#NOTE that dictionaries have no order so no index just key value pair
#key value pair called item
dictionary.items() #will return pair like this dict_items([('shinno',22), (etc.)])


dictionary = {
  "shinno":["A", 21],
  "aimi":["A", 22]
}

second_dictionary = {
  "shinno":{"bloodtype":"A", "age":21},
  "aimi":{"bloodtype":"B", "age":22}
}

dictionary["shinno"][0] == second_dictionary["shinno"]["bloodtype"]

#print(something, something_else)




#--------------------------------
#While LOOPS!!!!!
#while condition:
  # code...

while True:
  print("hello")

while 2 > 1:
  print("whats up")


#keep your code DRY, never repeat
number = 1
while number <= 10:
  print(number)
  number += 1
#will return number 1..10

#loops to add to list
L = []

while len(L) < 3:
  new_name = input("please add a new name: ").strip().capitalize()
  L.append(new_name)

print("list is full")
print(L)




#creating a range:
range(1,11)
#will return [1,2,3,4...10] up to but not including eleven
#note that it outputs a range iterable not a list!!!!
range(1,11,2) #will return [1,3,5,7,9]

# for loops
#similar to each in ruby (even though ruby also have for loops)
for number in range(1,1001):
  print(number)

for letter in "abcd":
  print(letter)
#will return "a", "b", "c", "d" because strings are iterable datatypes


#list comprehensionnnnnnnnn

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)


odd_numbers = [x for x in range(1,101) if x % 2 != 0]
print(odd_numbers)


words = ["hello", "hi", "hey", "yo", "heya"]
output = [[w.upper(), w.lower(), len(w)] for w in words]
print(output)
#will return [['HELLO', 'hello', 5], ['HI', 'hi', 2], ['HEY', 'hey', 3], ['YO', 'yo', 2], ['HEYA', 'heya', 4]]

#same thing as:
words = ["hello", "hi", "hey", "yo", "heya"]
output = []
for w in words:
  output.append([w.upper(), w.lower(), len(w)])
print(output)
#but the method above keeps it clean







#NOOTEEESSSSS
# in if else or while or for loops these keywords are important:
pass
break
continue





#functions
def add(x,y):
  return x + y

def add(x,y):
  print(x + y)


# the functions above are not the same!!!!!
# returning something and printing something is different
# printing just displays something
# return actually outputs something
# so if you wanna store it in a variable:
# answer = add(5,10)
# then if it returns then answer == 15
# BUT if the function only prints then answer will == nil


# function that returns reverse of strings
def reverse(string):
  return string[::-1]








#SCOPES IN FUNCTIONS

#global scopes --> varibles that can be accessed anywhere

a = 100

def f1():
  print(a)

def f2():
  print(a)

# will print 100 two times if you run this
# because varibale a is defined outside of any function
# thus being globally accessible


#local scope --> varibales that can only be accessed inside certain functions

def f1():
  a = 100
  print(a)

def f2():
  print(a)

#will only print out a for first function
#because second function cannot access a because its only accessible in f1



#global variable vs. local variable

a = 250

def f1():
  a = 100
  print(a)

def f2():
  a = 50
  print(a)

f1() #--> 100
f2() #--> 50
print(a) #--> 250

#global variables cannot be modified inside local scopes
#thus python creates a new varibale with the same name in this case
#so the global variable a
#and the local variable inside f1 called a
#and the local variable inside f2 called a
#are ALL different variables



#HOWEVER if you want to change a global variable from inside a local scope
#then you can use the global keyword

a = 250

def f1():
  global a #this line has to be separate. cannot do global a = 100 in one line
  a = 100
  print(a)

def f2():
  a = 50
  print(a)

f1() #--> 100
f2() #--> 50
print(a) #--> 100

# now global variable is 100 because it was overridden in f1



#however a small part of a global variable can be changed if using lists

a = [1,2,3]

def f1():
  a = 100
  print(a)

def f2():
  a = 50
  print(a)

f1() #--> 100
f2() #--> 50
print(a) #--> [1,2,3]

#but you can change elements inside the list

a = [1,2,3]

def f1():
  a[0] = 99999
  print(a)

def f2():
  a = 50
  print(a)

f1() #--> [99999,2,3]
f2() #--> 50
print(a) #--> [99999,2,3]

#thus global variable was partially overridden without using global keyword





#arguments order and default value

def about(name, age):
  sentence = "my name is {} and i am {} years old".format(name, age)
  return sentence

about("shinno", 21)
#returns "my name is shinno and i am 21 years old"

# but you can also do
about(age = 21, name = "shinno")
# which also returns "my name is shinno and i am 21 years old"

#however what if you dont want to put an age?
#it will give an error 'wrong number of arguments'
#thus we will put a default value

def about(name, age = 'undefined'):
  sentence = "my name is {} and i am {} years old".format(name, age)
  return sentence

about(name = "shinno")
#will return "my name is shinno and i am undefined years old"


#NOTE HOWEVER PARAMETERS WITH DEFAULT ARGUMENTS NEED TO GO LAST
def about(name, age = 'undefined'):
  sentence = "my name is {} and i am {} years old".format(name, age)
  return sentence

# but cannot do
def about(age = 'undefined', name):
  sentence = "my name is {} and i am {} years old".format(name, age)
  return sentence






#---------------
#packing unpacking *args and *kwargs
print(1,2,3)
#returns 1 2 3

# however if we do this
list = [1,2,3]
print(list)
#it will return [1,2,3] which is the list itself not the elements

#BUT we can do this
print(*list) #which unpacks the list revealing all its elements
#and returns 1 2 3

#another example
print("a", "b", "c") == print(*"abc")
#but
print("a", "b", "c") != print("abc")


# useful for passing arguments to functions
#if we just do
def add(x,y):
  return x + y

#then we are limited to only passing two arguments in the function
#what if we want a whole list of numbers to be added?
#then

def add(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

add(1,2,3,4,5,6,7,8,9)
#works and returns 45 because it unpackages the arguments


#BUT CANNOT DO THIS!!
numbers = [1, 2, 3, 4, 5, 6]
#or
numbers = (1, 2, 3, 4, 5, 6)
add(numbers)
#will return error because list and tuple are unpackaged directly


#using dictionary to create key value pair and thus ignore argument order
def about(name, age, hobby):
  sentence = "its {}! they are {} years old and they like {}".format(name, age, hobby)
  return sentence

dictionary = {"hobby":"soccer", "name":"shinno", "age":23}
about(**dictionary)
#returns "its shinno! they are 23 years old and they like soccer"


#how do we do the reverse? it called packing!
def foo(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}".format(key, value))

foo(shinno = "male", aimi = "female")
#prints out shinno:male aimi:female
