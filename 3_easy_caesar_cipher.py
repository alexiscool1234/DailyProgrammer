# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

import string

word = list(raw_input("Please enter your top secret spicy meme: "))
rot = int(raw_input("Please enter the number of rots: "))
alphabet = string.lowercase
newwordindex = []
newwordchars = []
char = 0

for i in word:
    char = string.lowercase.index(i)
    for x in range (0,rot):
        char += x
    newwordindex.append((char % 26 + 1))

for z in newwordindex:
    for i,c in enumerate(alphabet):
        if i == z:
            newwordchars.append(c)

print ''.join(newwordchars)
