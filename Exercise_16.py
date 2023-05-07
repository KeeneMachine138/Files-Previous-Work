#!/usr/bin/env python
# coding: utf-8

# In[3]:

ratings = open('rating.txt')
lines = ratings.readlines()
num_lines = len(lines)
ratings.close()
print(lines)
low_rating = []
for l in lines:

    print(float(l))
    r = float(l)

    if r < 7.0:
        print("Y0uR rAtinG iS BeLow 7")
        print(r)
        low_rating.append(r)

print("Total number of low ratings is: ", len(low_rating))
print("Total number of lines: ", num_lines)

lowfile = open('lowrating.txt', 'a')
for r in low_rating:
    lowfile.write(str(r))
lowfile.close()

# In[6]:


import csv

userrating = {}

##Reading file
with open('userrating.csv', 'r') as csvfile:
    ratings = csv.reader(csvfile, delimiter = ',')
    row_counter = 0
    for r in ratings:
        print(r)
        print(



##Writing file
with open('jokerrating.csv', 'w', newline = '') as csvfile:
    jokerrating = csv.writer(csvfile)
    j_ratings = []

# In[ ]:




