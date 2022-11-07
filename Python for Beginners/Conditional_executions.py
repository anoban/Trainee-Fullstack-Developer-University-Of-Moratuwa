from datetime import datetime

datetime.now().ctime()

# if condition:
    # statement1
# else:
    # statement2

# or

# if condition:
    # statement1
# elif condition2:
    # statement2
# elif condition3:
    # statement3
# else:
    # statement4

evens = list(); odds = list()
for i in range(0,1001):
    if i % 2 == 0:
        evens.append(i)
    elif i % 2 == 1:
        odds.append(i)
    else:
        print("i is equal to ".format(i))

odds
evens

# perfecto! :)

# indentation is not essential when the conditioned execution statements are given
# in the same line as the condition!

mark = 55
if mark <= 39: grade = 'D'
elif mark < 55 : grade = 'C'
elif mark < 70 : grade = 'B'
else: grade = 'A'
print (grade)

