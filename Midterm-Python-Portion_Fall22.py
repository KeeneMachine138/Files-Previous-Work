# The following is the programming section of this exam
# Total points are out of 25pts
# Please work on this template, and upload your answers to Canvas when complete

# Q1.(3pts) Write a program that outputs a winking smiley face (use your own artistic interpretation!):

print("         ")
print(" o    -  ")
print("   <     ")
print(" \_____/ ")

# Q2.(3pts) Write code to take in a user's first name, last name, and school major, separately and then print it to the screen together as shown below
# Enter first name: John
# Enter last name:  Smith
# Enter school major: English
# Output: John Smith, English Major

user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")
school_major = input("Please enter your major for School: ")

users_output = [user_first_name, user_last_name, school_major]
print(users_output)

# Q3.(6pts) Write a function that returns the first and last letters of a string
# For example, when I pass aardvark into the function, I should return a string with only two letters example ak 
def first_and_last(word):
    return word[0] + word[-1]

print(first_and_last("aardvark"))

# Q4.(6pts) Write a function that will continue to multiply numbers  from user input, the number of numbers to take in comes from a parameter
def multiply_num(number):
    i = 1
    num = []
    for i in range(number):
        total = float(input('Enter a number: '))
        new_total = total * new_total
        num.append(new_total)
    return num


amount = 5
multiply_total = multiply_num(amount)
print(multiply_total)

# Q5. (7 pts) After taking Bus Adm 335, the CIA has recruited you to write a function that unscrambles a sequence of characters into readable english.
# The function takes in two parameters, the scrambled string, and the indices of the corresponding letters in the string to unscramble it
# EX unscramble("hlleo wrodl",[0,2,3,1,4,5,6,8,7,10,9]), returns "hello world"

def unscramble(scrambled_string, list_indices):
    unique_characters = []
    unique_letters = 0
    for ch in word:
