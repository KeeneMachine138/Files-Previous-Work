# In class Variable Naming Prac
       
num_anim_mil_zoo = 5000
user_fav_ice_crm_flav = "chocolate"
txtbk_desc = "A wonderful introduction to python"
hrs_std_slp_sem = 600
class_name = 'bus adm 335'
user_tshrt_sz = "medium"


# Variable Description Prac

abc_corp_rev = 150000
john_sal = sam_sal = dave_sal= 70000
mike_sal = 70100
strt_sal_anyst, sen_sal_anyst, man_sal = 70000, 90000, 100000

print(abc_corp_rev)
print(john_sal,sam_sal,dave_sal)
print(mike_sal)
print(strt_sal_anyst, sen_sal_anyst, man_sal)

# 'type' & 'id' Command Prac

print('num_anim_mil_zoo')
print(type(num_anim_mil_zoo))
print(id(num_anim_mil_zoo))

print('user_fav_ice_crm_flav')
print(type(user_fav_ice_crm_flav))
print(id(user_fav_ice_crm_flav))

print('txtbk_desc')
print(type(txtbk_desc))
print(id(txtbk_desc))

print(type(hrs_std_slp_sem))
print(id(hrs_std_slp_sem))

print(type(class_name))
print(id(class_name))

print(type(user_tshrt_sz))
print(id(user_tshrt_sz))

# Data Types
# Intergers ('int') and Strings ('str')

x = 1
print(type(x))
y = -2
print(type(y))
z = "Boring classes kill me"
print(type(z))
a = "1"
print(type(a))

# 'float' commands or decimal numbers

print(float(1))
print(float(4))
print(float(2943))

my_float = 1.299183742
print('{:.2f}'.format(my_float))
print('{:.4f}'.format(my_float))

my_float = 1.299183742
print('{:.4f}'.format(my_float))
print('{:.5f}'.format(my_float))

my_float = 5.098649174
print('{:.4f}'.format(my_float))
print('{:.7f}'.format(my_float))

# Order of Operations and Expressions

x = 9000
y = -3560
z = 4
a = 2
print(2*(x - (x + 2 + y)))
print(a**z)
print(z**a)

# 'index', 'length'(len), & 'replace' command

cat_1_name = 'Cheeto Puff Fluff'
cat_2_name = 'Coco Puff Fluff'
tv_show = 'Rick & Morty'

print(cat_1_name)
print(len(cat_1_name)) # Tells how long the string is
print(cat_1_name[2])   # Tells the letter at that position 
print(cat_1_name[5])
print(cat_1_name[15])
print(cat_1_name.index('Fl')) # Tells the position of that part of the string
print(cat_1_name.index('P'))  # NOTE: Must match something that is exactly in
                              #       the original sting.
                              #       Example: If 'FL' was typed, would comeback
                              #                with error because 'FL' does not
                              #                exisit in the original string,
                              #                'Fl' does exist though.


print(cat_2_name)
print(len(cat_2_name))
print(cat_2_name[-2])
print(cat_2_name[10])
print(cat_2_name[-7])
print(cat_2_name.index('Fl'))
print(cat_2_name.index('co'))
print(cat_2_name.replace('Coco', 'Reeses'))
print(cat_2_name.replace('Puff', 'POOF'))


print(tv_show)
print(len(tv_show))
print(tv_show.index('Ric')) # Tells the number position of whats in the
                            #  parentheses
print(tv_show.index('&'))
print(tv_show.replace('Morty', 'MORTY'))
print(tv_show.replace('Rick', 'Larry'))

# Exercise 4
# Part 1: Write a code where user inputs total number of dimes and nickels
#         they have and adds them together

print("Please input total number of dimes you have")
dime_count = input("Total number of dimes: ")
print("Now please input total number of nickels you have")
nickel_count = input("Total number of nickels: ")
total_coins = int(nickel_count) + int(dime_count)
print("Your total number of coins are:", total_coins)

# Part 2: Write a program to compute how many gallons of paint are needed to cover a
#         user defined number of square feet of walls. Assume 1 gallon can cover
#         350.0 square feet. Output the result with 3 decimal digits

print('please input the total square feet of the wall you desire to paint')
sq_ft_wall = input ()
total_gal_of_paint = int(sq_ft_wall) * (1/350)
# print(total_gal_of_paint)
my_float = total_gal_of_paint
print('The total number of cans of paint you need is {:.3f}'.format(my_float))

# Part 3: Take in a student’s first three classes of the day and print 
#         them to a screen in one line.

print('Please write your class schedule')

class_1 = input('Class 1: ')
class_2 = input('Class 2: ')
class_3 = input('Class 3: ')
class_4 = input('Class 4: ')

print('Your current class list is:',class_1, class_2, class_3, class_4)

# Part 4: a) What are the 'indexes' of 'a' and 'D' in "I am a Developer".
#         b) What is the length of this string?
#         c) Change the value of "I am a Developer" to "I am a Programmer"

string_val = "I am a Developer"
print(string_val)
# Part 4 a):
print(string_val.index('a'))
print(string_val.index('D'))
print(string_val.index('ev'))
print(string_val.index('er'))

# Part 4 b):
print(len(string_val))

# Part 4 c):
print(string_val.replace('Developer','Programer'))
print(string_val)












