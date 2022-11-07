# syntax errors
# errors is the use of programming language

# runtime errors
# occurs during the execution of a Python script or a function

# logical errors
# errors in programme logic that would result in unexpected / erroneous behaviour
# logical errors would not throw any error messages


from gettext import npgettext
from math import radians
from operator import imod
from random import random
from secrets import choice


print("Hello world with syntax error!)
# SyntaxError: EOL while scanning string literal

# there are several types of runtime errors

# NameError
# TypeError
# IndexError
# ValueError
# ImportError

max(myList)
# NameError: name 'myList' is not defined

mylist = ["James", "Julian", "Hannah", "Chadwick", "Kravitz"]
mylist[5]
# IndexError: list index out of range

"TypeError" ** 8
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"TypeError" + 45
# TypeError: can only concatenate str (not "int") to str

import mymodule
# ModuleNotFoundError: No module named 'mymodule'

# ValueError occurs when a built-in Python function receives an argument with compatibe data type
# with invalid value!
int("invalid value")
# ValueError: invalid literal for int() with base 10: 'invalid value'
int("4")
# 4 - works just fine!


# handling runtime errors
# programme execution will terminate when a runtime error occurs
# for the programme to continue execution after the runtime errors, these errors need to be 
# handled appropriately

# try except block is used to handle runtime errors in Python
# here the code block where errors are anticipated to occur is passed inside the try block
# and if any errors occur within a try block Python will simply jump to the next
# expression without terminating the programme execution


mylist = ["Hannah", "Susanne", "Julia", 5, "Jeanne", "Jennifer", 9, "Samantha", "Leslie", "Beverly"]

# IndexError: index 200 is out of bounds for axis 0 with size 200

for i in range(10):
    print("Hi there! " + mylist[i] + "!")

try:
    for i in mylist:
        print("Hi there!", i + "!")
except:
    print("Unsupported data type encountered!")
# halts the iteration at number 5 in the list and executes the except block!

for i in mylist:
    try:
        print("Hi there!", i + "!")
    except:
        continue
# finishes the iteration completely, skipping numerics!

raise MemoryError("Hahahah fuzzy memory error!")
raise KeyboardInterrupt("Some fucker pressed Ctrl + C")
raise IndexError("Get a grip dumbass")

for i in mylist:
    try:
        print("Hi there!", i + "!")
    except:
        continue
    finally:
        print("This block executes no matter what!")
        # this line will be executed even when the loop skipped the expressions in the try block!

# a try block can have 0 or more except blocks!


