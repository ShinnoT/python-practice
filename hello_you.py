#personal notes
#input() is the same as gets.chomp in ruby
#must save input() in a variable


#ask user for name
name = input("What is your name?: ")
#ask user for age
age = int(input("What is your age?: "))
# print(type(age)) --> <class 'int'>
#ask user for city
city = input("Which city do you live in?: ")
#ask user what they enjoy
hobby = input("What do you enjoy doing in your free time?: ")
#create output text
output = "hello {0}, I am from {2} as well! I love {3} as well omg. you will be {1} next year".format(name, age+1, city, hobby)
#print output to screen
print(output)




#string concatination and interpolation in python
#A = "blah"
#B = "blob"
# A + B
# will return "blahblob"

#"="*5
#will return "====="

#however, cant add different types (it wont convert implicitly)

#string formatting (same as string interpolation in ruby)
# "{} - {}".format(A,B)
# will return "blah - blob"

# "{} - {}".format(B,A)
# will return "blob - blah"
# OR you can do it this way
# "{1} - {0}".format(A,B)
# will return "blob - blah"

