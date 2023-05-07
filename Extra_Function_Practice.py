# Extra Function Practice

def function_1():
    print('ahhh')
    print('ahhhhhhhhh 2')
print("This is outside of the function")

function_1()

function_1()
function_1()

def function_2(x):
    return 2 * x

z = function_2(5)
print(z)
a = function_2(3)
print(a)

b = function_2(23)
print(b)

def function_3(x, y):
    return x + y

e = function_3(4,9)
print(e)
f = function_3(2,1029)
print(f)
ewww = function_3(1,1)
print(ewww)

def function_4(y):
    print(y)
    print('Still aint shit!!!')
    return y + 3 + (y**2)
g = function_4(4)
print(g)

# Function - BMI Calculator

name1 = "Y2K"
height_m1 = 6
weight_kg1 = 90

name2 = "Y2K's Brother"
height_m2 = 8
weight_kg2 = 125 

name3 = "Y2K's cousin"
height_m3 = 4
weight_kg3 = 125

def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ", bmi)
    if bmi < 25:
        return name + ' is not overwieight'
    else:
        return name + ' you one chunky monkey'

result_1 = bmi_calc(name1, height_m1, weight_kg1)
print(result_1)
print("The first results are for:", name1)

result_2 = bmi_calc(name2, height_m2, weight_kg2)
print(result_2)
print("The first results are for:", name2)
    
result_3 = bmi_calc(name3, height_m3, weight_kg3)
print(result_3)
print("The first results are for:", name3)

def rick_n_morty(y):
    print(y)
    print("Your Breathe be HAWT")
    x = float(input("Enter a number dummy: "))
    return y + 3 + (x*y)
rick_n_morty(7)
wwe_smackdown = rick_n_morty(7)
print(wwe_smackdown)

def function_5(some_arg):
    print(some_arg)
    print("weeeeee")
function_5(4)
function_5("Eatin a twinky")
