# for the following program, what is the namespace for each name?
# i.e. global, local, built-in
# player_name: 
# roll: 
# number: 
# str: 

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




# pt 2
# Recommendation


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




#pt 3
# date formatter
# print european or american dates
# set default for day, month, year to 1,1,2000 and format American

def print_date():
    pass

