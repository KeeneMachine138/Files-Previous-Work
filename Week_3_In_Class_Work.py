# List- Container of data

example_list = ['first_example', 'second_example', 'third_example']
print(type(example_list))
print(example_list)


# Lists can hold elements of many types
#   |__> Integers, Strings, Floats and lists

tv_shows = ['Rick & Morty', 'Modern Family', 'Game of Thrones']
fav_foods = ['Dino Nuggets', 'Cheese Curds', 'Cookies']
num_list = [1,1,2,2,3,3,4]

lists_of_lists = [tv_shows, fav_foods, num_list]

print(lists_of_lists)

# Lists can be mutable(ie changeable)

ex_list = [10, 100, 100, 10000]
print(ex_list)
ex_list[2] = 1000
print(ex_list)

# Lists can be 'index'

another_ex_list = ["dino nuggets", 20, 3.05, 'Mac n Cheese']
print(len(another_ex_list))
print(another_ex_list)
print(another_ex_list[0])
print(another_ex_list[-1])
print(another_ex_list[3])

# Lists can added on to; the 'append' command

random_list = ["dino nuggets", 'Game of Thrones', 3.208, 7, 'Gameboy']

print(random_list)
random_list.append('GameCube') # only adds element to the end of the list
print(random_list)

# Elements can be removed from a list: use 'pop' or 'remove' commands

nintendo_game_sys = ['Gameboy', 'Nintendo Entertainment System', 'SNES', 'GameCube','Wii', 'Switch']

print(nintendo_game_sys)
nintendo_game_sys.pop(1) # pop removes the value at index position/location
print(nintendo_game_sys)
nintendo_game_sys.pop(0)
print(nintendo_game_sys)
nintendo_game_sys.pop(-1)
print(nintendo_game_sys)

best_game_sys = ['Gameboy', 'Nintendo Entertainment System', 'SNES', 'GameCube','Wii', 'Switch']

print(best_game_sys)
best_game_sys.remove('Wii') # Removes a value from a list by a specific value
print(best_game_sys)
best_game_sys.remove('SNES')
print(best_game_sys)

# Other list operations:
#       len(list):          Find the length of the list
#       list1 + list2:      Produce a new list by concatenating list2 to the end 
#                           of list 1
#       min(list):          Find the element with smallest value in the list
#       max(list):          Find the element with the largest value
#       sum(list):          Find the sum of all elements of a list (numbers only)
#       list.index(val):    Find the index of the first element in list whose 
#                           value matches val
#       list.count(val):    Count the number  of occurrences of a value in the 
#                           list

# Booleans - the 'True' and 'False' of python

print(type(True))
print(type(False))

boolean_list_1 = [1,2,3,4]
print(bool(boolean_list_1))

boolean_list_2 = []
print(bool(boolean_list_2))

# 'isinstance' command and booleans

print(isinstance(boolean_list_1, list)) # Returns 'True' or 'False based what is in the
                                        # parentheses (obj, type), if correct, then 'True'
                                        # if incorrect then 'false'

print(isinstance(boolean_list_1, int))
print(isinstance(boolean_list_1, str))

# Exercise 5

# Part 1: Find the highest and lowest number in the list, also find the sum of the list

making_lists = [72, 17, 12, 18, 41, 32, 64, 36, 22, 15]

print(max(making_lists))
print(min(making_lists))
print(sum(making_lists))

# Part 2: Scottify has hired you to work on their playlist feature.
#         Make a list of the songs and the artisit

song_1 = 'Never Gonna Give you Up'
song_2 = 'Party All the Time'
song_3 = 'Ice Ice Baby'
song_4 = 'Power of Love'
song_5 = 'Mmmbop'
song_6 = input("please input a song 6: ")
song_7 = input("please input a song 7: ")

artist_1 = 'Rick Astley'
artist_2 = 'Eddie Murphy'
artist_3 = 'Vanilla Ice'
artist_4 = 'Huey Lewis and the News'
artist_5 = 'Hanson'
artist_6 = input("please input a artist 6: ")
artist_7 = input("please input a artist 7: ")

playlist = [[song_1,artist_1], [song_2,artist_2], [song_3,artist_3], [song_4,artist_4], [song_5,artist_5]]

print(playlist)

playlist.append(song_6)
playlist.append(artist_6)
playlist.append(song_7)
playlist.append(artist_7)

print(playlist)

# User interactive Playlist

song_1 = input("please input a song 1: ")
song_2 = input("please input a song 2: ")
song_3 = input("please input a song 3: ")
song_4 = input("please input a song 4: ")
song_5 = input("please input a song 5: ")

artist_1 = input("please input a artist 1: ")
artist_2 = input("please input a artist 2: ")
artist_3 = input("please input a artist 3: ")
artist_4 = input("please input a artist 4: ")
artist_5 = input("please input a artist 5: ")

new_playlist = [[song_1,artist_1], [song_2,artist_2], [song_3,artist_3], [song_4,artist_4], [song_5,artist_5]]

print(new_playlist)

