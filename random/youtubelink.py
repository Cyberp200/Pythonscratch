# youtubelink.py

# bunch of amth functions and stuff

# 20220112

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
from pytube import YouTube

# DEBUG TITLE
print("\n\nyoutubelink.py\n.\n.\n.\n.\n\n")

# MAIN
video = YouTube(https://youtu.be/Uamp8cdZed0)

stream = video.streams.get_highest_resoltuion()

stream.download()
