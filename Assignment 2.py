# Use the print function to print a smiley face to the screen.
# Your design can look like this, or a design of your choosing.
print("")
print("Q1, Smiley Face")

print(" o    o ")
print("   <    ")
print("        ")
print("\      /")
print(" \____/ ")

# Use the print function to print an arrow, using ^
print("")
print("Q2, Up Arrow")

print("    ^    ")
print("   ^ ^   ")
print("  ^ ^ ^  ")
print(" ^ ^ ^ ^ ")
print("   ^ ^   ")
print("   ^ ^   ")

# Take in a user’s favorite food and output the results to the screen
print("")
print("Q3 user's favorite food")

print("Hello my friend \nwhat is your favorite food?")
fav_fd = input()
print("Ah, I see your favorite food is", fav_fd)

# An investor is interested in how much money they are going to make a
# year from an investment in vending machines. The projections vary.
# Write a program that takes in daily net profit from the user and displays
# the equivalent yearly net profit.
# Hint: Yearly net profit = daily net profit X 365, for example daily profit
# of $1 is $365 yearly, also be aware of type from your input function).
print("")
print('Q4: print the formula')

print('please input the daily profit received from the vending machine:')
daily_net_profit = input ()
total_yearly_net_profit = float(daily_net_profit) * (365)
my_float = total_yearly_net_profit
print("Your yearly profit is:", '{:.3f}'.format(my_float))

      
