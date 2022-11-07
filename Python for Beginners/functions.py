# syntax, parameters & return values of functions in Python

# function call / invocation is the use of pre-defined functions in the standard library
# function definition is the creation of custom functions by users

# advantages of functions:
# beter code resuability 
# better modularity for programmes (a refined programme structure)

# inputs takes by function are called argumenst or parameters
# outputs returned by functions can be captured in variables

# function syntax
# def function_name (parameters):
    # docstring (optional)
    # function statements
    # return value/expression (optional)

def counter (input_list):
    """Returns the counts of each unique elements in the
    supplied container object, as a Python dictionary."""
    input_list = list(input_list)
    mydict = dict()
    for i in input_list:
        if i in mydict.keys():
            mydict[i] += 1
        elif i not in mydict.keys():
            mydict[i] = 1
    return mydict


import numpy as np
import itertools
from string import ascii_letters
import random

rints = np.random.choice(range(21), size = 100, replace = True)
rchars = [random.sample(ascii_letters, k = 1) for i in range(200)]
rchars = list(itertools.chain(*rchars))
rchars

mylist = list(rints) + rchars

results = counter(mylist)
type(results)
results.keys()
results.values()

def greeting ():
    name = str(input("Enter your first name!"))
    print("Hello there! {}!".format(name))

greeting()

# if the number of arguments that will be passed to a function is unknown,
# * can be passed in with the arguments
# myfunc(*params)
#       for param in params:
#           # statements