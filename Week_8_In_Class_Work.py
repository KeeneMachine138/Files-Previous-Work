val = 0
sum_val = 0
while val != -1:
    sum_val = sum_val + val # Can also be written as: sum_val += val
    val = float(input('Please input another number: '))
print('sum of all input numbers are {}'.format(sum_val))
    
