# human interaction with computers involve I/O
# that is input & output
# this interaction does not necessarily has to be with a human
# but can be with another computer

# Python's default input() helps take inputs from user via the terminal
# this input() also supports an optional prompt

usr_input1 = str(input("Enter your first name!"))
usr_input2 = str(input("Enter your last name!"))
print("Your full name is {}. {}.".format(usr_input2, usr_input1))

# by default Python accepts the terminal input as a string
iput = input("Want to know the default data type of inputs?")
iput        # '12.475e-1.254'
type(iput)  # <class 'str'>

# if we need to obtain a numerical input from terminal as a number,
# this will by default be received as a string which needs to be typecasted to an integer!

numeric_age = int(input("Enter your age!"))
numeric_age   # 25

# the default output function print() takes keyword args to customize the output
print("Sarah","Natalie","Hanna","Beverly")
# Sarah Natalie Hanna Beverly
# all elements are printed in the same line, separated by a space!

print("Sarah","Natalie","Hanna","Beverly", sep = "*")
# Sarah*Natalie*Hanna*Beverly

print("Sarah","Natalie","Hanna","Beverly", sep = "\t")
# Sarah   Natalie Hanna   Beverly

print("Sarah","Natalie","Hanna","Beverly", sep = "\n")
# each name is printed in a new line

# the end keyword arg determines the ending element of the output
# if nothing is specified this end defaults to a newline character "\n" 
print("Hahaha", end = ":)") 
print("TeeHeee", end = ":))) \n")

# formatting print statements
print("Nadia's mom passed away on {}.".format(("05.28.2016")))
# Nadia's mom passed away on 05.28.2016.