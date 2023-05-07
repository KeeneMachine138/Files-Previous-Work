# 'if', 'else', & 'elif' Commands

# 'if' Commands

x = int(input("please input a number: "))
if x > 5:
    x = x + 2
print(x)

# 'if' & 'else' commands

x = int(input("please input x variable: "))
y = int(input("please input y variable: "))
z = int(input("please input z variable: "))

if x + z > y:
    print(x + z)

else:
    print(y)

# 'if', 'else' and 'elif' commands

birth_year = int(input('please input your birth year: '))

if birth_year < 1996:
    print ("You were born before 1996")
elif birth_year == 1996:
    print ("You were born in 1996")
else:
    print ("You were born after 1996")

# multiple 'if' commands

age = int(input('please input your age: '))
if age > 16:
    print('You are old enough to drive')
if age > 18:
    print('You are old enough to vote')
if age > 21:
    print('You are old enough to drink')
if age > 25:
    print('You are old enough to rent a car')

# 'if', 'else', 'elif' practice
# hotel practice problem

hotel_rate = 155
age = int(input('Please enter age: '))
if age > 65:
    hotel_rate -= 20
print('Your hotel rate is:', hotel_rate)

# hotel practice problem 2

age = int(input('Please input your age: '))
bed_type = 'King'
if age > 65:
    if bed_type == 'King':
        hotel_rate = 135
    else:
        hotel_rate = 125
else:
    if bed_type == 'King':
        hotel_rate = 155
    else:
        hotel_rate = 145
print('Your Hotel Rate is', hotel_rate)

# Exercise 6 Write a program that:
    # Asks the user to input 3 numbers
    # Outputs the maximum number of the three

num_1 = float(input('please input a first number: '))
num_2 = float(input('please input a second number: '))
num_3 = float(input('please input a third number: '))

if num_1 > num_2:
    max_num = num_1
else:
    max_num = num_2
if max_num < num_3:
    max_num = num_3
print('The maximum number you input is', max_num)

# Execise 6 - using 'and' 'or' functions

num_1 = float(input('please input a first number: '))
num_2 = float(input('please input a second number: '))
num_3 = float(input('please input a third number: '))

if num_1 > num_2 and num_1 > num_3:
    max_num = num_1
else:
    max_num = num_2
if num_3 > num_1 and num_3 > num_2:
    max_num = num_3
print('Your max number is: ', max_num)

# Exercise 7 Part 1
# Verifying a Trusted email

user_email = input('Please enter your email: ')

if '@uwm.edu' in user_email:
    print('We trust this email')
else:
    print('This person a fake')

# Exercise 7 Part 2
# Shopping cart list practice

shopping_cart = ['beer', 'diapers', 'frozen-pizza', 'toothpaste', 'bread', 'peanut butter']

if 'beer' in shopping_cart:
    if 'diapers' not in shopping_cart:
        print('Buy some diapers')
    else:    
        print('you have the diapers')
if 'pizza' and 'ice cream' in shopping_cart:
    if 'chocolate' not in shopping_cart:
        print('We recommend you buy some chocolate')
    else:
        print('you already have chocolate')
if 'bread' or 'peanut butter' in shopping_cart:
    if 'milk' in shopping_cart:
        print('you have the milk')
    else:
        print('got milk?')
    


