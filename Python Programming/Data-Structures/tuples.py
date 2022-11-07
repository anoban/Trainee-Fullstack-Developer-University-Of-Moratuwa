from asyncio import events
import imp


mystr = "Starboy is the third studio album by Canadian singer-songwriter the Weeknd"
# lists are ordered data types
weeknd_list = list(mystr)
weeknd_list

# sets aren't so
weeknd_set = set(mystr)
weeknd_set

# tuples are immutable!
# tuples are ordered as well
# paranthesis are not mandatory in declaring tuples

mytuple = (1,2,3,"My",'Hello',78)
mytuple_wo_paranthesis = 2,3,67.65564564E-7,"Jasmine"
mytuple
mytuple_wo_paranthesis

weeknd_tuple = tuple(mystr)
weeknd_tuple

# tuple packing
packed_tuple = 1,2,3,4.5434253E2, 4.67E10, "Janice"
packed_tuple

# tuple unpacking
a,b,c,d,e,f = packed_tuple
a
b
c
d
e
f

evens = tuple(range(0,200,2))
len(evens) # 100

# index based extraction
evens[45]
evens[78]
evens[-1]
evens[-99]

# slicing
evens[3:45]
evens[:12]
evens[:]
evens[80:]
evens[:-50]
evens[-50:]

# nested tuples
ntuple = tuple(list(range(0,100,5))+list([(23,45,("James","Jhonathan","Amelia"),12,"A")]))
ntuple
# (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, (23, 45, ('James', 'Jhonathan', 'Amelia'), 12, 'A'))
ntuple[-1] # (23, 45, ('James', 'Jhonathan', 'Amelia'), 12, 'A')
ntuple[-1][-3] # ('James', 'Jhonathan', 'Amelia')
ntuple[-1][-3][2] # 'Amelia'

# tuples consume less memory compared to lists in Python
import sys
mytuple = tuple(["James","Jhonathan","Amelia","Kyle","Jennifer","Peter","Penny","Jackovick"])
mylist = list(["James","Jhonathan","Amelia","Kyle","Jennifer","Peter","Penny","Jackovick"])
# both have identical elements
sys.getsizeof(mytuple) # 104 bytes
sys.getsizeof(mylist) # 120 bytes

# tuple multiplication
(1, 3, 4, 5) * 4
# this does not multiply each element by 4 like R vectors
# here the whole sequence is repeated 4 times

(1,2,3,4) + (3,4,5,6)
(3,4,5,6) + (1,2,3,4) 
