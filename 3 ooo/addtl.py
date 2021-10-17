# addtl.py

# named as addtl.py due to being tbd content

# 20211006

# Patrick Chung
# cyberp200@rocketmail.com
# 562-480-2114

'''
              ___.                       _______________  _______
  ____ ___.__.\_ |__   _________________ \_____  \   _  \ \   _  \
_/ ___<   |  | | __ \_/ __ \_  __ \____ \ /  ____/  /_\  \/  /_\  \
\  \___\___  | | \_\ \  ___/|  | \/  |_> >       \  \_/   \  \_/   \
 \___  > ____| |___  /\___  >__|  |   __/\_______ \_____  /\_____  /
     \/\/          \/     \/      |__|           \/     \/       \/

'''

# Imports

import sys
import math
import random
import threading
import time
from functools import reduce

# DEBUG TITLE
print("\n\naddtl.py\n.\n.\n.\n.\n\n")

str1 = "Escape Sequences \' \" \t \\ \n"

# So these things were always called escape sequences, the things that allows
#   things like single and double quotes and newlines and tabs to be used
#   inside strings.
# List of escape sequences
#   \'      makes the apostrphe
#   \"      makes the quotation
#   \\      makes the backslashes
#   \t      makes the tabs
#   \n      makes newline

#Practice zone

print("EXAMPLE\n")

print("does print() automatically create a newline?")
print("lets find out")

print("\nso apparently it does, so how do we get it to print without newline?")

print("here is one line", end = "")
print("here is another\n\napparently python3 print() needs an additional argument to make it not newline.")
print(" what must be typed is this print(\"here is a line\", end = \"\")\n like wtf.")

print("\nEXAMPLE of sep=\'\'\n")
print(1,2,3,4,sep=",")

print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'), end = '\n\n')

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data, end = '\n\n')


# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


'''
MORE ON Strings
'''

# RAW STRINGS

print(r"I'll be ignoring escape sequences in this string like this \t\n")

# String concatenates

print("\nHello " + "World")

# SPECIAL STRING FUNCTIONS TO PARSE STRINGS WITH

# String length

stringEx = "Hello fucker"

print("Using len() to get length of string ->", len(stringEx), "The string was", stringEx)

# Return specific character in string

#   get the first character
print('getting the first character, use stringEx[0] ->', stringEx[0])

#   get the last character (its pretty simple)
print('getting the last character, use stringEx[-1] ->', stringEx[-1])

#   getting just the 'e' in the word "fucker"
print('getting the \'e\' in \"fucker\", use stringEx[-2] ->', stringEx[-2])
#       doing it again using the other direction of the char array
print('getting the \'e\' in \"fucker\", but in the opposite direction, use stringEx[10] ->', stringEx[10])

#   get a range of characters displayed
print('getting the \'Hello\', or the first 5 characters, use stringEx[0:5] ->', stringEx[0:5])
print("Up to but not include the 5th index")

#   get a range of characters displayed
print('getting only every other character, use stringEx[0:-1:2] ->', stringEx[0:-1:2])
print("the 0 and the -1 is the range, and the 2 is the increment in which to skip up to")
