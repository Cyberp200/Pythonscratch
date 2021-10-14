# cond.py

# bunch of amth functions and stuff

# 20211011

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
print("\n\ncond.py\n.\n.\n.\n.\n\n")


# IF STATEMENT

x = int(input("Type some fucking number -- "))

if x > 21:
    print("x is greater than 21")
elif x >= 16:
    print("x is greater or equal to 16")
else:
    print("fuck....")

'''
You will notice that in python3

if x > 21:
(TAB) print("x is greater than 21")
elif x >= 16:
(TAB) print("x is greater or equal to 16")
else:
(TAB) print("fuck....")


Python3 must use tabs and nextlines in this exact
configuration for conditionals to function properly.

else if is elif
'''

# BOOLEAN OPERATORS AND VALUES

# the operators that we can use are
#   and
#   or
#   not

x = int(input("Type some other fucking number -- "))

if x < 5:
    print("x is less than 5")
elif (x >= 5) and (x <= 6):
    print("x greater or equal to 5 and also less than or equal to 6")
elif (x == 69):
    print("How many days till Christmas?", x)
else:
    print("fuck.... again.....")


# and is used as such,


# TERNARY OPERATOR

# Allows for variable assigment using boolean operators

# https://www.geeksforgeeks.org/ternary-operator-in-python/
#
a, b = 10, 20

canVote  = a if a >= b else b

print("\n\nThis is the ternary operator, using boolean logic to assign variables, the number that got assigned is", canVote)


print("\n\n\n\n\n\n\n")
