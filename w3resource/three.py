# three.py

'''
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''

# 20211123

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

# Non-standard Imports
import datetime

# DEBUG TITLE
print("\n\nthree.py\nw3resource\n.\n.\n.\n.\n\n")

now = datetime.datetime.now()

timendate = now.strftime("%Y-%m-%d %H:%M:%S")
#print("Time is relative:\n" + timendate)

# REMIXED ANSWER
x=int(timendate[11:13])
if x > 12:
    pm = str(x-12)
    print(timendate[:11] + pm + timendate[13:] + "pm")
else:
    am = str(x)
    print(timendate[:11] + am + timendate[13:] + "am")
