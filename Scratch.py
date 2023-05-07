class Song:
    def __init__(self, song_title, song_artist):
        self.song_title = song_title
        self.song_artist = song_artist
    def __str__(self):
        return "Song Name: {} \nArtisit Name: {}".format(self.song_title,self.song_artist)

class Playlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.queue = []

    def add_song(self, song):
        self.queue.append(song)

    def play(self):
        while len(self.queue) > 0:
            print("Now Playing:")
            song = self.queue.pop(0)
            print(song)
    def __str__(self):
        return "Playlist: {}\nOwner: {}".format(self.name, self.owner)


s1 = Song("Never Gonna Give you Up", "Rick Astley")
s2 = Song("Party All the Time", "Eddie Murphy")
s3 = Song("Power of Love", "Huey Lewis and the News")

my_playlist = Playlist("Gage's Fiesta Mix", "Scott")

my_playlist.add_song(s1)
my_playlist.add_song(s2)
my_playlist.add_song(s3)
my_playlist.play()

class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = (self.salary * percent) + self.salary
    def work(self):
        print("Place Holder")
    def __str__(self):
        return ("This employee's Name is: {}\nThis employee's salary is: {}".format(self.name, self.salary))
        

class Chef(Employee):
    def __init__(self, salary = 500000):
        
        self.salary = salary
class Server(Employee):
    pass
class PizzaRobot(Employee):
    pass
class Customer:
    pass
class Oven:
    pass

