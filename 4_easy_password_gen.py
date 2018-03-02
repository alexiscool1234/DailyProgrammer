# https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
# plus extras

import string
from random import *

length = int(raw_input("Please enter the length of the desired password: "))
number = int(raw_input("How many passwords would you like? "))
alphabet = string.lowercase + string.uppercase + string.digits + string.punctuation
scrambledindex = []
scrambled = []

for i in range(0,number):
    for i in range(0,length):
        scrambledindex.append(randint(1, len(alphabet)))
    for si in scrambledindex:
        for i,c in enumerate(alphabet):
            if i == si:
                scrambled.append(c)

    print ''.join(scrambled) # print passwords
    del scrambledindex[:] # empty list
    del  scrambled[:] # empty list
