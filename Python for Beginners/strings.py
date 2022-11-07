# strings are immutable

name = "Python"
name[0] = "p"
# TypeError: 'str' object does not support item assignment
# strings are immutable

# string concatenation
name + " v.3.10.4"
name + " v.3.10.4" + " AMD64 bit"

# string replication
"Replica" * 10
"Replica with a trailing space " * 5
"Hi with a new line \n" * 10
"Hello\tthere!" * 5

# Python does not support char data type
# so "" & '' both used to define strings
# 'A' is just a string with one element! not a character data type

it2 = "IT Chapter 2 was a pretty stupid movie"
it2[9:]
it2[:9]
it2[8]
it2[-11:-3]

it2.lower()
it2.upper()
len(it2)

"T" in it2
"Q" not in it2
# string data type in Python supports membership operators as well

# string formatting using % operator

print("My name is %s and I'm from %s" % ("George", "Canton"))
print("Nadia is a %s and she is %d years old" % ("waitress", 27))
print("%d to the power of %d, equals to %f" % (2,2,4))

