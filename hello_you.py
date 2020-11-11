# ask the user name

name = input("What is your name? ")

#ask the user age

age = input("How old are you? ")

print(name, "\n",     age)

#ask user the city

city = input("Where do you live? ")

#ask user what they enjoy

love = input("What do you like to do? ")

#output text

string = "Your name is {} and you are {} years old. You live in {} and you like to {}."
output = string.format(name, age, city, love)

#print output

print(output)

