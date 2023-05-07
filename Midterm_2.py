# Q1. (5 pts): Create a tuple, my_tuple, with the following customer data:
# "John Smith", "123 ABC St", 55555

my_tuple = ('John Smith', '123 ABC St', 55555)
print(my_tuple)

# Q2. (5 pts): Write a program that takes in your a user's favorite course, and writes it to a file, bestclass.txt
# EX Output: Input favorite class: Bus Adm 335
#            favorite course written to bestclass.txt

# user_fav_course = input('Please Input your favorite class: ')

user_fav_class = str(input("Please input your favorite Class: "))

bestclass = open("bestclass.txt","w")
bestclass.write(user_fav_class)
print(" We have updated bestclass.txt with the user's favorite class! ")
bestclass.close()

#Q2. (5pts) Write the following avocado data to a CSV file called avocados.csv

import csv

my_data = [
    ["Date","AveragePrice","Total Volume","4046","4225","4770","Total Bags","Small Bags","Large Bags","XLarge Bags","type","year","region"],
    ["12/27/2015","1.33","64236.62","1036.74","54454.85","48.16","8696.87","8603.62","93.25","0","conventional","2015","Albany"],
    ["12/20/2015","1.35","54876.98","674.28","44638.81","58.33","9505.56","9408.07","97.49","0","conventional","2015","Albany"],
    ["12/13/2015","0.93","118220.22","794.7","109149.67","130.5","8145.35","8042.21","103.14","0","conventional","2015","Albany"]
    ]

with open('avocados.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile)
    for row in my_data:
        data.writerow(row)

    data.writerows(my_data)
print("It ain't easy, being cheesy")


# Challenge Questions Pick 1 of the two
# Q4. (10 pts): Write a program that maintains a movie list and has two classes, movie and movie list
# Movie: has three attributes, movie_name, and duration, and  when the object is printed it will display "Movie Name: movie name attribute, Duration:  movie duration attribute"
# MovieList: has three attributes: owner(creator of list), movie_list_name (name of list), and movie_list(holder of task objects)
# MovieList also has a method add_movie, which adds a single movie to the movie_list, and a method clear() which clears out all tasks within a movie list
# Finally, use the defined classes by creating two movie objects of your choosing, add them to a movie list object, then clear the movie list
class Movie:
    pass

class MovieList:
    pass
          
           
#Q4 (10pts) Write a class associated with animals at a zoo
# 1) An Animal class that has a name and age property, and a speak method
# 2) 2 Animals of your choice (e.g. monkey, panda etc) that inherit the Animal class, and speak appropriately
# 3) A zoo class that has properties: name, and list of animals as well as a method to add animal objects to the list of animals
# 4) Create an instance of each of your animal classes and add them to an instance of your zoo class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("I'm an animal at the zoo!")
class Tropicalfish(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('YEET!')
class Panda(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('Munch Munch')
class Lion(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('Meow Meow')

class Zoo():
    def __init__(self, name, animals):
        self.name = name
        self.animals = animals 

my_panda = Panda("Rolly - Rolly", 6)
my_panda.speak()




