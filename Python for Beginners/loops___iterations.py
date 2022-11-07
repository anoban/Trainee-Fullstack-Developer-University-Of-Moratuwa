import numpy as np
np.random.seed(2022-4-17)
marks = np.random.choice(range(1,101), size=20, replace=False)
marks

# for loop is used when the number of needed itertions is known before
# while loops are better suited in iterations where the number of needed iterations are not known
# beforehand

grades = list()
for i in marks:
    if i >= 81:
        grades.append('A+')
    elif i >= 75:
        grades.append('A')
    elif i >= 60:
        grades.append('B')
    elif i >= 50:
        grades.append('C')
    elif i >= 35:
        grades.append('D')
    else:
        grades.append('F')

grades

# sum of all even numbers upto 100
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
sum  # 2550

n_input = int(input("Enter an integer!"))
n_input

i = 0
while i <= n_input:
    print(i**2)
    i += 1

i = 0
while i < 20:
    if i == 1:
        print("Hello world for the {} st time".format(i))
    elif i == 2:
        print("Hello world for the {} nd time".format(i))
    elif i > 2:
        print("Hello world for the {} th time".format(i))
        if i == 10:
            break
    i += 1

for i in range(100):
    while i < 20:
        print("The number is {}".format(i))
        break # break the while loop when i >= 20

# break statement is used to exit the loop suddenly without looping until the end
# of the iterable!
# a break statement should always be passed inside an if
# otherwise a loop will break away at the very first iteration

for i in range(10):
    print(i)
    break
# prints just 0

for i in range(10):
    break
    print(i)
# nothing gets printed

for i in range(10):
    if i == 5:
        break
    print(i) 
# prints from 0 to 4

# continue is used to skip the downstream statements of the loop body and jump to
# next iteration!

for i in range(10):
    if i == 5:
        continue
    print(i)
# prints every number from 0 to 9 but 5

for name in names:
    if name[0] == 'V':
        print("Hi there! {}!".format(name))
    elif name[0] == 'N': # skips printing Natalie
        continue
    print(name) # this statement won't be executed when name[0] == 'N'

# similar to break, continue should also be placed inside an if
# otherwise loop will just jump to next iterations without executing any downstream statements

for i in range(10):
    print(i)
    continue
    print(i*2) # this line will never be executed

# pass is just a placeholder that does nothing
# usually used during experimental loop constructions
# to avoid indentation errors

i = 0
while i < 10:
    pass

for i in names:
    pass

# else can also be used in while loops

i = 0
while i < 10:
    print("i is equal to {}. Still less than 10 :) ".format(i))
    i += 1
else:
    print("Oops!. Now i is equal to {}".format(i))

rands = np.random.choice(range(1001), size=2000, replace=True)
rands

i = 0
while rands[i] != 5:
    i += 1
else:
    print("5 is found at index {}".format(i))

rands[367]   

numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    print(count)
    if number==1:
        break
else:
    count=-1
print(count)

num = 5
while (num !=0):
    num = num - 1 
    if (num == 2): 
        continue
    print ("Hello World!")

# prime number detection

num = int(input("Enter an integer!"))

if num == 1 or num == 0:
    print("not a prime")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime")
    else:
        print("prime")