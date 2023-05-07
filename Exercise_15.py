# Part 1 Create a tuple with the following data from a database:
# (name, birthdate, address, state, zip)
# John Smith, 1-1-1970, 123 Fake St, WI, 55555
my_tuple = ('John Smith', '1-1-1970', '123 Fake St', 'WI', 55555)
my_list = tuple(['John Smith', '1-1-1970', '123 Fake St', 'WI', 55555])

print(my_tuple)
print(my_list)

# Part 1 create a set from the following string "AAABCCC"
# What do you notice?
my_str = "AAABCCC"
my_set = set(my_str)
print(my_set)

# Part 1 Use the set() builtin function to create a user defined function that takes in a word,
# and returns the unique number of characters
def unique_letters(word):
    uniq = len(set(word))
    return uniq

print(unique_letters('apple'))

# Given a list of words that represents a text
# Count how many words are in the text, store these counts in a dictionary.
# What is the most common word?

text_example = "It was the best of times, it was the worst of times, it was the age of\
wisdom, it was the age of foolishness, it was the epoch of belief, it \
was the epoch of incredulity, it was the season of Light, it was the \
season of Darkness, it was the spring of hope, it was the winter of \
despair, we had everything before us, we had nothing before us, we were \
all going direct to Heaven, we were all going direct the other way--in \
short, the period was so far like the present period, that some of its \
noisiest authorities insisted on its being received, for good or for \
evil, in the superlative degree of comparison only. \
There were a king with a large jaw and a queen with a plain face, on the \
throne of England; there were a king with a large jaw and a queen with \
a fair face, on the throne of France. In both countries it was clearer \
than crystal to the lords of the State preserves of loaves and fishes, \
that things in general were settled for ever. \
It was the year of Our Lord one thousand seven hundred and seventy-five. \
Spiritual revelations were conceded to England at that favoured period, \
as at this. Mrs. Southcott had recently attained her five-and-twentieth \
blessed birthday, of whom a prophetic private in the Life Guards had \
heralded the sublime appearance by announcing that arrangements were \
made for the swallowing up of London and Westminster. Even the Cock-lane \
ghost had been laid only a round dozen of years, after rapping out its \
messages, as the spirits of this very year last past (supernaturally \
deficient in originality) rapped out theirs. Mere messages in the \
earthly order of events had lately come to the English Crown and People, \
from a congress of British subjects in America: which, strange \
to relate, have proved more important to the human race than any"

text_example = text_example.lower()
text_example = text_example.replace(",","")
text_example = text_example.replace(".","")
text_example = text_example.replace("(","")
text_example = text_example.replace(")","")
text_example = text_example.replace(":","")
# converts the string to a list

string_to_list = text_example.split(" ")
print(string_to_list)

# unique words in list
unique_words = set(string_to_list)
print(unique_words)

# initialize the keys into the dictionary
word_ct_dict = {}
for word in unique_words:
    word_ct_dict[word] = 0
print(word_ct_dict)

# count the unique terms
for word in string_to_list:
    word_ct_dict[word] += 1
print(word_ct_dict)

highest_word = "N/A"
highest_freq = 0
for word, freq in word_ct_dict.items():
    if freq > highest_freq:
        highest_freq = freq
        highest_word = word
        
print(highest_freq)
print(highest_word)
