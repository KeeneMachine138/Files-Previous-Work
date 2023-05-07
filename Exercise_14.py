# input 5 numbers

x=5

def make_calculations():
    global x
    numbers = []
    while x > 0:
        new_num = float(input("Input number: "))
        numbers.append(new_num)
        x -= 1
    sum_num = 0
    for x in numbers:
        sum_num += x
    mean = sum_num/len(numbers)
    print("Mean is :",mean)
    biggest_num = numbers[0]
    smallest_num = numbers[0]
    for x in numbers:
        if x > biggest_num:
            biggest_num = x
        if x < smallest_num:
            smallest_num = x
    print("Biggest number:",biggest_num)
    print("Smallest number:",smallest_num)
    
    range_numbers = biggest_num - smallest_num
    print(range_numbers)

make_calculations()
        
        
