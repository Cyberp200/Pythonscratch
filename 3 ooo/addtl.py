# addtl.py

# named as addtl.py due to being tbd content

# 20211025

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

print("EXA\vMPLE\n")

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


# Here are some basic string argument specifiers you should know:

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

# Replacing index VALUES
print("\nUsing the (string var name).replace(\"(string segment)\",\"(new string segment)\") function\n")

stringEx = stringEx.replace("Hello", "Goodbye")
print(stringEx, "\n")

stringEx = stringEx.replace("Good", "Bad")
print(stringEx, "\n")

stringEx = stringEx.replace("e f", "E Fffffff")
print(stringEx, "\n")

# Snip Strings with concats and indexing

print("Snip and concatenate strings with fancy indexing.")
print("stringEx = stringEx[:1] + \"y\" + stringEx[0:]\n")


stringEx = stringEx[:1] + "y" + stringEx[0:]
print(stringEx, "\n")

#   [:1] is everything up to the 2nd index [1] and [0:] is everything after the
#   first index

# STRING SEGMENT CHECKS

print("\nCHECK TO SEE IF A CERTAIN STRING SEGMENT EXISTS IN EXISTING STRING")
print("\nIs there \"By\" in stringEx", "By" in stringEx)
print("That statement will either return True or False\n\n")

print("\nIs there \"You\" in stringEx", "You" in stringEx)
print("\n")

print("\nIs there \"By\" not in stringEx", "By" not in stringEx)
print("\n")

# OTHER WAY TO CHECK segment

print("stringEx = \"Hello Garbage\"\n\nAnother way to find indexes of strings segments\n")
stringEx = "Hello Garbage"

print("Hello index", stringEx.find("Hello"), end='\n\n')
print("Garbage index", stringEx.find("Garbage"), end='\n\n')

# Trim White Space

print("          This string has stripped white space.         ".strip())

# Convert List to a string

print(" ".join(["some", "words"]))
#   takes the space from the " ".join and separates list items in the string

# Convert String to a List
print("A string".split(" "))
#   takes a strings and uses the space in the .split(" ") to separate the string into list items


# and f string for formatted output
print("f string for formatted output")
print("int1 = 1\nint2 = 2")
int1 = 1
int2 = 2
print('print(f\"{int1} + {int2} = {int1 + int2}\")')
print(f"{int1} + {int2} = {int1 + int2}")

# Convert Uppercase to lowercase and visa versa
print("Convert uppercase to lower case an visa versa with \"A STrinG\".lower() or \"A STrinG\".upper()")
print("OG string is \"A STrinG\"")
print("A STrinG".lower())
print("A STrinG".upper())

# Convert Uppercase to lowercase and visa versa
print("Convert uppercase to lower case an visa versa with \"A STrinG\".lower() or \"A STrinG\".upper()")
print("OG string is \"A STrinG\"")
print("A STrinG".lower())
print("A STrinG".upper())

# Check if string is either a character or a numbers
print("Functions for check for numbers or characters")

print("\"AString123\".isalnum() -> ","AString123".isalnum())
#   is it all numbers and alphabetical chars?
print("\"AString123\".isalpha() -> ","AString123".isalpha())
#   is it just alphabetical chars?

print("\"123\".isdigit() -> ","123".isdigit())
#   is it all numbers and alphabetical chars?
print("\"String\".isalpha() -> ","AString".isalpha())
# Interstingly, spaces and puncuation make this return false
