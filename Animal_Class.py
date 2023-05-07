class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self):
        print("Hi there, I'm an animal")


class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('Bark Bark')

class Parakeet(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('Sqwuak!')

class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('Meow Meow')
        
class Goldfish(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print('YEET!')
        
my_dog = Dog("Fido",7)
my_dog.speak()

my_bird = Parakeet("Chirpie", 5)
my_bird.speak()

my_cat = Cat("Cheeto Puff", 3)
my_cat.speak()

my_goldfish = Goldfish("Goldy",1)
my_goldfish.speak()
