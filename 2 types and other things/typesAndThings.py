# typesAndThings.py

# Multiline programming or single line programming with multiple lines.
# variable flexibility in python
# types
# casting


# 20211002

# Patrick Chung
# ppchung2018@hotmail.com
# 562-480-2114

'''
                    _       _                             _
   ____            (_)     | |                           | |
  / __ \ _ __  _ __ _ _ __ | |_ _ __   ___ _ __ __ _  ___| | __
 / / _` | '_ \| '__| | '_ \| __| '_ \ / __| '__/ _` |/ __| |/ /
| | (_| | |_) | |  | | | | | |_| | | | (__| | | (_| | (__|   <
 \ \__,_| .__/|_|  |_|_| |_|\__|_| |_|\___|_|  \__,_|\___|_|\_\
  \____/| |
        |_|

In Atom IDE with "atom-python-run" package installed, press F5 to run.
'''

# --- main ---

v1 = 1 + 2 + 3
# typical single line statement

print("1. v1 =", v1)
#debug for line 27

v1 = (
    1 + 2
    + 3
    )
# example of a single statement over multiple lines with paranthesis binding it

print("2. v1 =", v1)
#debug for lines 33 - 36

v1 = 1 + 2 \
    + 3
# example of a single statement over multiple lines with with a back slash

print("3. v1 =", v1)
#debug for lines 42 - 43

v1 = 5; v2 = v1 + 1
#two statements, one line

print("4. v1 =", v1, ", v2 =", v2)
# each parameter for print() concatenates to each other separated by a space
# debug for line 52

# VARIABLES
#   - can either start with a letter or an underscore

v1 = 1
V1 = 2
# vars are case sensitive
_v1 = 3

print("5.",v1, V1, _v1)
# debug for lines 59 - 61

v3 = v4 = 4
# You can instantiate variable mid statement while assigning it to another var

print("6.",v3, v4)

#---------------------------------------------

v = 1

print("7.",v)

v = "triple x"

print("8.",v)
# You can assign a new type to the same variable

'''
Basic types in python
    ints
    floats
    complex numbers
    strings
    bools
    (there are more, but these are basic)
'''

'''
Ways to find types
type()
    - this fn will take a value and find its default type
'''

print("9. 10",type(10))
print("10. 10.1",type(10.1))
print("11. Hello",type("Hello"))
print("12. True",type(True))

'''
Ways to find types
sys.maxsize
    - this will return the max size for an integer type
    - must "import sys" to use this function
'''

import sys
print("13. int max size", sys.maxsize)

print("14. float max size", sys.float_info.max)

'''
COMPLEX NUMBERS
'''

cn1 = 5 + 6j

print("15. complex numbers", cn1)

'''
bools
'''

bool1 = True
bool2 = False

print("16. Booleans", bool1, bool2)

'''
Strings
    - and how to format them
'''

string1 = "Escape Sequnce as it is called \' \" "
# using the backslash on the single quote and double quote allows it to be
# displayed in the string console display

print("17. Strings", string1)

string2 = 'can use single quotes for strings \' \" '

print("18. single quote Strings", string2)

string3 = 'tabs in strings \t tabbed, then backslashes \\ then newlines \n new lined'
# These are the main Escape sequences
print("19. tabs:", string3)

string4 = ''' This one is wierd, no need for backslashes for single and double quotes ' " '''
# Can make string using 3 single quotes, which allows the use of single and double quotes normally
print("20. Triple quote strings:", string4)


print("21. Cast 5.4 to int -->", int(5.4), type(int(5.4)))
print("22. Cast 5.4 to string -->", str(5.4), type(str(5.4)))
print("23. Cast 97 to character -->", chr(97), type(chr(97)))
#there is no char type in Python, but wtf chr(2) is apparently a happy face
print("24. Cast \"a\" to int -->", ord("a"), type(ord("a")))
