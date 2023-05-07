# Loops

# While loops

# Example 1
val = 0
sum_val = 0
while val >= 0:
    sum_val += val # Can also be written as: sum_val = sum_val + val  
    val = float(input('Please input another number: '))
print('sum of all input numbers are {}'.format(sum_val))

# Example 2
val = 0
sum_val = 0
while val != -1:
    sum_val = sum_val + val # Can also be written as: sum_val += val
    val = float(input('Please input a number to continue and -1 to exit: '))
print('sum of all input numbers are {}'.format(sum_val))

# Example 3 - Couting Loops
val = 0
sum_val = 0
i = 1
N = 3
while i <= N:
    val = float(input("Please Enter a number: "))
    sum_val = sum_val + val
    i = i + 1
print("Sum of all numbers you input are: {}".format(sum_val))

# Exercise 10

# Create a for loop with enumerate function to implement this game where 
# each character of the two strings is compared
#   For each matching character, add one point to user_score
#   Upon a mismatch, end the loop

user_score = 0
simon_input = input('Please input a 5-character sequence of R, B, G, Y for Simon: ')
user_input = input('Please repeat Simons sequence: ')

for idx, ch in enumerate(user_input):
    if simon_input[idx] == ch:
        print ('Match at:', idx, ch)
        user_score = user_score + 1
    else:
        break

print(user_score)

def print_pattern():
    print('******')

print_pattern()
print_pattern()
print(print_pattern)

# Exercise 11

# Write a function that converts Celsius to Fahrenheit

def temp_conversion(C):
    F = C * 9 / 5 + 32
    return F
print(temp_conversion(22))

# Exercise 12

##Functions
def get_unique_letters(word):
    # returns the unique letters in a word
    # apple, has 4 unique letters
    unique_chars = []
    unique_letters = 0
    # use a loop to loop through word and count the unique letters
    for ch in word:
        if ch not in unique_chars:
            unique_chars.append(ch)
    unique_letters = len(unique_chars)
    return unique_letters

print(get_unique_letters("apple"))
unique = get_unique_letters("apple")
#get_un

def get_numbers(times):
    x = 1
    numbers = []
    # takes a parameter of times to ask for a number
    # appends numbers to a list and returns them
    for x in range(times):
        value = float(input('Enter a number: '))
        numbers.append(val)
                      
    return numbers
get_numbers(5)

def print_positive_numbers(numbers):
    # Print positive numbers
    pass


def print_negative_numbers(numbers):
    # Print all negative numbers
    pass

##Main Program
unique_letters = get_unique_letters("apple")

size = 5
list_numbers = get_numbers(size)
print_positive_numbers(list_numbers)
print_negative_numbers(list_numbers)

