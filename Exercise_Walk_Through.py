# Exercise 1
print("This is my first line of code")
print("Get off my lawn")
import os
print("Homework grade is:", 5 * 8 + 23)

# Exercise 2
# Part 1
print("    No Parking    ")
print("2:00am - 6:00am")

print("   NO PARKING   \n2:00am - 6:00am")

# Part 2
print("    ^    ")
print("   ^ ^   ")
print("  ^ ^ ^  ")
print(" ^ ^ ^ ^ ")
print("^ ^ ^ ^ ^")

print("  $  \n $ $ \n$ $ $")

# Part 3
# Option 1

print("Hello Friend!")
print("Pleae input your zipcode: ")
zipcode =  input()
print("The zipcode you entered is:", zipcode)

# Option 2

print("Hello Friend!, Another way to enter a zip code")
zipcode =  input("Pleae input your zipcode: ")
print("The zipcode you entered is:", zipcode)

# Exercise 3
# Part 1 - Create Variable names for the following descriptions

# Number of animals at the Milwaukee zoo, 500
num_anml_mke_zoo = 500
print(num_anml_mke_zoo)

# User’s favorite ice cream (flavor, chocolate
usr_fav_ice_crm_flv = 'chocolate'
print(usr_fav_ice_crm_flv)

# Textbook descriptions, A wonderful introduction to python
txt_bk_desc = 'A wonderful introduction to python'

# Hours a student sleeps in a semester, 600
hrs_std_sleep_sem = 600

# class name, "bus adm 335"
cls_nm = 'bus adm 335'

# user's t shirt size -  use 'input' function
user_t_shirt = input("Please input your t-shirt size: ")

# Part 2 - Create variable names for the following descriptions

# Use different variable assignment methods to assign values to variables
# ABC Corp made 150000 in revenue
# John, Sam and Dave all made the same salary last year 70000
# While Mike make 70100
# The starting salary for analyst, senior analyst and manager are:
# 70000, 90000 and 100000

abc_corp_rev = 150000
jon_sal = sam_sal = dave_sal = 70000
# mike_sal = 70100
mike_sal = jon_sal + 100
analyst, sr_analyst, mgr = 70000, 90000, 100000

print(jon_sal)
print(sr_analyst)
print(mike_sal)

# Part 3 - Use the 'type()' and 'id()' functions to print the type of object, and
#          memory address

# example
# print("name_var")
# print(type(name_var))
# print(id(name_var))

print("num_anml_mke_zoo")
print(type(num_anml_mke_zoo))
print(id(num_anml_mke_zoo))

print("num_anml_mke_zoo")
print(type(num_anml_mke_zoo))
print(id(num_anml_mke_zoo))
        
# Exercise 4
# Part 1 - Take how many nickels and dimes the user has and add them together
# Option 1

print("Hello my guy")
print("Please input the number of nickels you have: ")
nickels = int(input())
print("Now please input the total number of dimes you have: ")
dimes = int(input())
total_coin_count = nickels + dimes
print("The total number of coins you have is: ", total_coin_count)

# Option 2

print("Hello my friend, this is another way to count the total number of coins you have")
nickels = int(input("Please input the number of nickels you have: "))
dimes = int(input("Now please input the total number of dimes you have: "))
total_coin_count = nickels + dimes
print("The total number of coins you have is: ", total_coin_count)

# Part 2 - Write a program that converts the square feet int how many gallons of paint a user needs
# 1 gallon of paint = 350 Square Feet

print("Hello friend, I will be helping you find how many gallons of paint\nyou need based on the area of the wall in square feet")
wall_area = float(input("Please type in the wall area in square ft: "))
gal_per_sqft = 1/350
gal_needed = wall_area * gal_per_sqft
print("You will need {:.3f}" .format(gal_needed), "gallons of paint")

# Part 3 - Take in the users classes and create a list

first_class = input("Please input your first class: ")
second_class = input("Please input your second class: ")
third_class = input("Please input your third class: ")

# cls_schedule = first_class +" "+ second_class +" "+ third_class
cls_schedule = first_class, second_class, third_class
print(cls_schedule) 

# Part 4
# What are the indexes of a and D in "I am a Developer"?

str_val = "I am a Developer"
print(str_val.index('a'))
print(str_val.index('D'))
print(str_val[2],str_val[7])
print(str_val[-4], str_val[-8])

# What is the length of this string?

print(len(str_val))
str_length = len(str_val)
print(str_length)

# How would you change the value of "I am a Developer" to "I am a Programmer"
print(str_val.replace("Developer", "Programer"))
print(str_val)
str_val = str_val.replace("Developer", "Programer")
print(str_val)

# Exercise 5
# Part 1 - Suppose you have a list of 10 numbers
# [72, 17, 12, 18, 41, 32, 64, 36, 22, 15]
# Find the HIGHEST and LOWEST number in the list, also find the sum

num_list = [72, 17, 12, 18, 41, 32, 64, 36, 22, 15]
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# Part 2a
# Scottify has hired you to work on their playlist feature.
# With Python make a playlist of these 5 songs:

play_list = [['Never gonna give you up', 'Rick Astley'],
             ['Party all the TIme','Eddie Murphy'],
             ['Ice Ice Baby','Vanilla Ice'],
             ['Power of Love','Huey Lewis & the News'],['Mmmbop','Hanson']]

print(play_list)

# Part 2b - Create a user input driven song entry

user_playlist = []

song_1 = input('Enter song 1: ')
artist_1 = input('Please Enter artist for this song: ')
user_playlist.append([song_1, artist_1])
# song_pairing_1 = song_1, artist_1 --> ANOTHER OPTION: '#' above
# user_playlist.append(song_pairing_1)  Line of code
print(user_playlist)

song_2 = input('Enter song 2: ')
artist_2 = input('Please Enter artist for this song: ')
user_playlist.append([song_2, artist_2])
print(user_playlist)

song_3 = input('Enter song 3: ')
artist_3 = input('Please Enter artist for this song: ')
user_playlist.append([song_3, artist_3])
print(user_playlist)

song_4 = input('Enter song 4: ')
artist_4 = input('Please Enter artist for this song: ')
user_playlist.append([song_4, artist_4])
print(user_playlist)

song_5 = input('Enter song 5: ')
artist_5 = input('Please Enter artist for this song: ')
user_playlist.append([song_5, artist_5])
print(user_playlist)

user_playlist.pop(0)
print(user_playlist)
song_6 = input('Enter song 6: ')
artist_6 = input('Please Enter artist for this song: ')
user_playlist.append([song_6, artist_6])
print(user_playlist)

user_playlist.pop(0)
print(user_playlist)
song_7 = input('Enter song 7: ')
artist_7 = input('Please Enter artist for this song: ')
user_playlist.append([song_7, artist_7])
print(user_playlist)

# Part 3 - Check the first and last songs on the playlist
#          to make sure they are 'list' type
#          |--> use 'isinstance' command

print(isinstance(user_playlist[0], list))
print(isinstance(user_playlist[-1], list))

# Exercise 6 - 'if', 'elif', and 'else'
#               Write a program that asks the user for 3 inputs
#               and gives output of the max number.

num_1 = float(input('Please input the a number: '))
num_2 = float(input('Please input the another number: '))
num_3 = float(input('Please input the a third number: '))

if num_1 > num_2:
    max_num = num_1
else:
    max_num = num_2
    
if num_3 > max_num:
    max_num = num_3

print(max_num)

# Option 2

num_1 = float(input('Please input the a number: '))
num_2 = float(input('Please input the another number: '))
num_3 = float(input('Please input the a third number: '))

if num_1 > num_2:
    if num_1 > num_3:
        max_num = num_1
    else:
        max_num = num_3
elif num_2 > num_3:
    max_num = num_2
else:
    max_num = num_3

print(max_num)

# Option 3 - using 'list' functions/commands

num_1 = float(input('Please input the a number: '))
num_2 = float(input('Please input the another number: '))
num_3 = float(input('Please input the a third number: '))

my_nums = [num_1, num_2, num_3]
max_num = max(my_nums)
print('Your max number is: ', max_num)

# Part 2 - Rewrite exercise 6 using 'and' 'or' booleans values

num_1 = float(input('Please input the a number: '))
num_2 = float(input('Please input the another number: '))
num_3 = float(input('Please input the a third number: '))

if num_1 > num_2 and num_1 > num_3:
    max_num = num_1
elif num_2 > num_1 and num_2 > num_3:
    max_num = num_2
else:
    max_num = num_3

print(max_num)

# Exercise 7
# Part 1 - check a users email using 'if' and 'in' commands

user_email = input('Please input you email address: ')

if 'uwm.edu' in user_email:
    print('We can trust this email')
else:
    print('This email is Shisty bro')

# Part 2 - Association Rule mining
# Write a program that recommends products to a users
# Requirement:  if the item already exists in the shopping cart,
#               do not recommend the item
# Patterns: 
#   - if a customer buys diapers, they also buy beer
#   - if a customer buys both frozen-pizza and ice cream, they will also buy a chocolate bar
#   - if a customer buys bread or peanut butter, they also buy milk

shopping_cart = ["beer","diapers","frozen-pizza","toothpaste", "bread","peanut butter"]

if 'diapers' in shopping_cart:
    if 'beer' not in shopping_cart:
        print('We recommend that you buy some beer')
    else:
        print('You gots the beer')
if 'frozen-pizza' in shopping_cart and 'ice cream' in shopping_cart:
    if 'chocolate' not in shopping_cart:
        print('We recommend that you buy some of dat chocolate')
    else:
        print("You get dat chocolate")
if 'bread' in shopping_cart or 'peanut butter' in shopping_cart:
    if 'milk' in shopping_cart:
        print('We recommend that you buy some milk.... GOT MILK BRO?')
    else:
        print('You have milk')

# Exercise 8 - Rewrite Exercise 6 program using loops

i = 1
N = 3
max_num = float(input("Enter in a number: "))

while i < N:
    print('Your i value is: ', i)
    val = float(input("Enter in a number: "))
    if val > max_num:
        max_num = val
    i +=1
print(max_num)

# Exercise 9 - More Loops Practice
# Part 1 - use 'for' loop to print "Python is Fun!" 15 times

for i in range(0,15):
    print(i, "Python is Fun!")

# Part 2 - Using our recommendation logic for the shopping cart recommendations
#          --> Same patterns/rules/recommendations for Items from Exercise 7

shopping_carts = [["beer","diapers","frozen-pizza","toothpaste", "bread","peanut butter"],
                  ["charcoal","milk","diapers","water", "chocolate bar"],
                  ["bread","ice cream","frozen-pizza","unreleased item"],
                  ["chips","diapers","frozen-pizza","ice cream", "bread"]]
# Use a 'for' loop to go through all of the shopping carts (lists within lists)
# within the 'shopping_carts' list
cart_index = 0

for shopping_cart in shopping_carts:
    print(shopping_cart)

    if "diapers" in shopping_cart and "beer" not in shopping_cart:
        print(cart_index, "We recommend that you buy beer")
    if "frozen-pizza" in shopping_cart and "ice cream" in shopping_cart and "chocolate bar" not in shopping_cart:
        print(cart_index, "We recommend that you buy a chocolate bar")
    if ("peanut butter" in shopping_cart or "bread" in shopping_cart) and "milk" not in shopping_cart:
        print(cart_index,"We recommend that you buy milk!")
    cart_index +=1

# Part 3 - An 'Unreleased Item' was added to one of the shopping carts by accident
#          and we need to figure out which cart it was added to 

cart_index = 0

for shopping_cart in shopping_carts:
    if 'unreleased item' in shopping_cart:
        print("Customer index: ", cart_index, "bought the unreleased item")
        print(shopping_cart)
        break
    cart_index += 1
print('Loop index:', cart_index)

# Exercise 10
# Create a Simon Says guessing game; use the 'enumerate' function

user_score = 0
simon_input = input('Please input a 5-Character sequenece of R, G, B, Y for Simon the guessing bot: ')
user_input = input('Please repeat Simon sequence: ')

for index, ch in enumerate(user_input):
    print(index,"user: ", ch, "simon:", simon_input[index])
    if ch == simon_input[index]:
        user_score += 1
    else:
        break
    
print('Your score of the game is', user_score)


mismatch = 0
simon_input = input('Please input a 5-Character sequenece of R, G, B, Y for Simon the guessing bot: ')
user_input = input('Please repeat Simon sequence: ')

for idx, ch in enumerate(user_input):
    print(idx,"user: ", ch, "simon:", simon_input[idx])
    if ch == simon_input[idx]:
        continue
    mismatch += 1

print('Your number of mismatches: ', mismatch)

# Exercise 11 - Intro in Functions
# Write a program to convert temperature from Celsius to Fahrenheit

def cels_to_fahr(c):
    f = c *(9/5) + 32
    return f
c = float(input('Please input temperature in Celcius: '))
f = cels_to_fahr(c)
print('Temperature in Fahrenheit is: ', f)

# Exercise 12 - Writing 'functions' practice

# Functions
def get_unique_letters(word):
    unique_chars = []
    unique_letters = 0
    for ch in word:
        print(ch)
        if ch not in unique_chars:
            unique_chars.append(ch)
    print(unique_chars)
    return len(unique_chars)

def get_numbers(num):
    i = 1
    numbers = []
    for i in range(num):
        val = float(input('Enter a number: '))
        numbers.append(val)
    return numbers

def print_positive_numbers(numbers):
    for num in numbers:
        if num >= 0 :
            print(num)
            
def print_negative_numbers(numbers):
    for num in numbers:
        if num < 0 :
            print(num)

# Main Program

# for 'get_unique_letters' function
unique_letters = get_unique_letters("apple")
print(unique_letters)

# for 'get_numbers' function
size = 5
list_numbers = get_numbers(size)
print(list_numbers)

# for 'get_positive_numbers' functions

print_positive_numbers(list_numbers)

# for 'get_negative_numbers' functions

print_negative_numbers(list_numbers)

# Exercise 13
# Part 1 - Random Number game

import random

player_class_tuple = ('Wizard', 'Elf', 'Human', 'Dwarf', 'Orc', 'Goblin')
print(player_class_tuple)

player_name = input('Please input your name: ')
player_class = input("Please select your player class from the list: ")

def roll():
    number = random.randint(1, 20)
    return number

print('A troll attacks')
troll_roll = roll()
player_roll = roll()

# print('Player: {}    Troll: {}'.format(str(player_roll), str(troll_roll)))
print('The player rolled a:', player_roll)
print('The troll rolled a:', troll_roll)

if player_roll < troll_roll:
    if player_class == 'Wizard':
        new_player_roll = player_roll + 3
        print('Your player_type is ' + player_class + ', you get plus 3 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
    if player_class == 'Elf':
        new_player_roll = player_roll + 4
        print('Your player_type is ' + player_class + ', you get plus 4 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
    if player_class == 'Human':
        new_player_roll = player_roll + 4
        print('Your player_type is ' + player_class + ', you get plus 4 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
    if player_class == 'Dwarf':
        new_player_roll = player_roll + 2
        print('Your player_type is ' + player_class + ', you get plus 2 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
    if player_class == 'Orc':
        new_player_roll = player_roll + 1
        print('Your player_type is ' + player_class + ', you get plus 1 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
    if player_class == 'Goblin':
        new_player_roll = player_roll + 1
        print('Your player_type is ' + player_class + ', you get plus 1 to your roll')
        print('The new roll for ' + player_name + ' is:', new_player_roll)
        if new_player_roll > troll_roll:
            print(player_name, 'has defeated the troll!')
        else:
            print(player_name, "has been defeated by the troll")
else:
    print(player_name, 'has defeated the troll!')

# Exercise 13 Part 2 
# put this recommendation logic into a function, and call it for each shopping cart
# print out the shopping carts before and after you run the function
def make_recommendation(shopping_cart):
    pass


if "diapers" in shopping_cart and "beer" not in shopping_cart:

    shopping_cart.append("recommendation: buy beer")
if "frozen-pizza" in shopping_cart and "ice cream" in shopping_cart and "chocolate bar" not in shopping_cart:
       
    shopping_cart.append("recommendation: buy chocolate")
if ("peanut butter" in shopping_cart or "bread" in shopping_cart) and "milk" not in shopping_cart:

    shopping_cart.append("recommendation buy milk")
   


shopping_carts = [["beer","diapers","frozen-pizza","toothpaste", "bread","peanut butter"],
                  ["charcoal","milk","diapers","water", "chocolate bar"],
                  ["bread","ice cream","frozen-pizza","unreleased item"],
                  ["chips","diapers","frozen-pizza","ice cream", "bread"]]

print(shopping_carts)




# Exercise Part 3
# date formatter
# print european or american dates
# set default for day, month, year to 1,1,2000 and format American

def print_date():
    pass
