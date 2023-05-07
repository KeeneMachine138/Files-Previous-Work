import random

# Functions

def set_game_difficulty():
    print('Welcome to the Word Guessing Game!')
    diff_options = input('Please select the difficulty level: Easy, Medium, or Hard: ')
    if diff_options == 'Easy':
        print('You selected difficulty level: ',diff_options)
        num_guesses = 10
        print('You get',num_guesses,'chances to guess the correct word')
    if diff_options == 'Medium':
        print('You selected difficulty level: ',diff_options)
        num_guesses = 7
        print('You get',num_guesses,'chances to guess the correct word')
    if diff_options == 'Hard':
        print('You selected difficulty level: ',diff_options)
        num_guesses = 5
        print('You get',num_guesses,'chances to guess the correct word')
    return num_guesses

def update_word_display(word, guess_list):
    word_display = []
    for guess_letter in word:
        if guess_letter not in guess_list:
            word_display.append("_")
        else:
            word_display.append(guess_letter)
    return word_display

def count_unique_letters(word):
    unique_chars = []
    unique_letters = 0
    for ch in word:
        print(ch)
        if ch not in unique_chars:
            unique_chars.append(ch)
    print(unique_chars)
    return len(unique_chars)

# Main Program

game_words_list = ['apple', 'banana']
game_word = random.choice(game_words_list)

guess_count = 0
guess_list = []
game_running = True
num_correct = 0
num_guesses = set_game_difficulty()

unique_characters = count_unique_letters(game_word)

while game_running == True:
    print("---------------------------------------")
    print('You have', num_guesses, 'guesses left')
    print('number correct:', num_correct, 'out of', unique_characters)
    print(update_word_display(game_word, guess_list))
    user_input = input('Enter your letter guess or type "quit" to quit: ')
    guess_list.append(user_input)
if user_input == 'quit':
    if user_input == 'quit':
        print('You have selected to quit the game')
        game_running = False

num_guesses -= 1
