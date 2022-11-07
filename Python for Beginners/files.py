# file handling in Python

file = open("mytextfile.txt")
# this just opens the file without loading its contents into memory!!
# an opening method can be specified when calling the open() function!

file.read() # to read in the contents to memory
# open() method returns an exhaustibe!  (an iterator)
# read() won't return any contents if called again after the first call
# unlike read() method, readline() method will not exhaust the iterator!

tennyson = file.read()
tennyson
print(tennyson)

# Mode   Description
			
# r	Opens a file for reading. (default)
# w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x	Opens a file for exclusive creation. If the file already exists, the operation fails.
# a Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t Opens in text mode. (default)
# b Opens in binary mode.
# +	Opens a file for updating (reading and writing)

open("mytextfile.txt", "r").writable() # False since the file is opened in reading mode
open("mytextfile.txt", "w").writable() # True :)
open("mytextfile.txt", "r+").writable() # also True

# .flush() method flushes the write buffer!

open("mytextfile.txt", "r+").read()
open("mytextfile.txt", "r+").readlines()
# .readlines() method returns a list of separate lines
# readline() method just prints a single line.

file = open("mytextfile.txt", "r") # iterator assigned to a variable
file.readline() # readline() will not exhaust the iterator object until all lines are read
file.close()

upper_tennsyson = file.read().upper()
upper_tennsyson
write_to = open("CAPITAL.txt", "w+")
write_to.write(upper_tennsyson)
write_to.close()

from string import ascii_letters
import random

rstring = ""
for i in range(10):
    #print(i)
    rstring += random.choices(ascii_letters, k = 1)[0]

rstring

myfile = open("writtenViaforloop.txt", "w+")
for i in range(100):
    rstring = ""
    for j in range(10):
        rstring += random.choices(ascii_letters, k = 1)[0]
    myfile.write("{} th random line is ".format(i) + rstring + "\n")
myfile.close()

myfile = open("writtelines.txt", "w+")
for i in range(100):
    rstring = ""
    for j in range(10):
        rstring += random.choices(ascii_letters, k = 1)[0]
    myfile.writelines("{} th random line is ".format(i) + rstring + "\n")
myfile.close()