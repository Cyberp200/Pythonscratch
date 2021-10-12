# mathtest.py

# bunch of amth functions and stuff

# 20211007

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
print("\n\nmathtest.py\n.\n.\n.\n.\n\n")

print("MATH STUFF\n")
print("5 + 2 =", 5+2)
print("")


# Shortcuts
i1 = 2
i1 += 1
print("i1 ", i1)

print('')

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) round up\t", math.ceil(4.5))
print("floor(4.5) round down\t", math.floor(4.5))
print("round(4.5) rounds down half and below only\t", round(4.5))
print("round(4.6) rounds down half and below only\t", round(4.6))
print("exp(1) e^1\t", math.exp(1))  # e^x where x = 1 here
print("log(e) math.log(math.exp(1))\t", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

ranNum = random.randint(1,101)

print(ranNum, "is a random number", end = '\n\n')

print("Is math.inf greater than zero", math.inf > 0)

print("\nWhat is math.inf minus math.inf. It is", math.inf - math.inf, "That means not a number")
