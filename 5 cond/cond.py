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

x = int(input("Type some fucking number"))

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
'''
