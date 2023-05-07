# Loops

# Comparing Strings
day = 'Tuesday'
print("day == 'Tuesday' returns", day == 'Tuesday')
print("day == 'tuesday' returns", day == 'tuesday')

# Exercise 8

N = 6
i = 1
max_num = float(input('Please input a number: '))

while i < N:
    val = float(input('Please input a number: '))
    if val >= max_num:
        max_num = val
    i += 1
print('Maximum value of your input is', max_num)

# Exercise 9
# Warm up
for phrase in range(15):
    print(phrase, 'pyhton is fun')

# Exercise 9 part 1
shopping_carts = [["beer","diapers","frozen-pizza","toothpaste", "bread","peanut-butter"],
                  ["charcoal","milk","diapers","water", "chocolate bar"],
                  ["bread","ice cream","frozen-pizza","unreleased item"],
                  ["chips","diapers","frozen-pizza","ice cream", "bread"]]

cart_index = 0
for cart in shopping_carts:
    print(cart)
    if 'beer' in cart:
        if 'diapers' not in cart:
            print('Buy some diapers')
        else:    
            print('you have the diappies')

    if 'pizza' and 'ice cream' in cart:
        if 'chocolate' not in cart:
            print('We recommend you buy some chocolate')
        else:
            print('you already have chocolate')
    if 'bread' or 'peanut butter' in cart:
        if 'milk' in cart:
            print('you have the milk')
        else:
            print('got milk?')
    cart_index +=1

# Exercise 9 part 2
shopping_carts = [["beer","diapers","frozen-pizza","toothpaste", "bread","peanut-butter"],
                  ["charcoal","milk","diapers","water", "chocolate bar"],
                  ["bread","ice cream","frozen-pizza","unreleased item"],
                  ["chips","diapers","frozen-pizza","ice cream", "bread"]]

cart_index = 0

for cart in shopping_carts:
    if 'unreleased item' in cart:
        print('Customer', cart_index, 'has the unreleased item')
        print(cart)
        break
    cart_index +=1 


    
