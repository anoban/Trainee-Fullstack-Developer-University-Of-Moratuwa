# lists are a container data type 
# unlike arrays Python lists can contain multiple data types, not a singular data type

vals = [i for i in range(0,10001)]
vals[46]
vals[67:69]
vals[-1]
vals[-12:-1]
vals[-547]
vals[:7]
vals[9998:]

new = list()
for i in range(564):
    new.append(i**2)

new

names = ["Anna", "Julie", "Joanne", "Natalie", "Sam"]
names[4] = "Sarah"
names

complex_nums = []

cplx = complex(45 + 59j)
cplx

for i,x in enumerate(range(1,11)):
    complex_nums.append(complex(i + x**2j))

complex_nums

names.remove("Sarah")
names
names.remove(names[2])
names

names.append("Venessa")
names.append("Monica")

# 2 dimensional lists
# a 5 x 5 list

twoD_list = list()
for i in range(1,6):
    nested = list()
    for j in range(1,6):
        nested.append(i**j)
    twoD_list.append(nested)

twoD_list

twoD_list[0][2]
twoD_list[2][1]
twoD_list[1][2]

del names[1]
names

names = names + ["Jeanne", "Samantha", "Beverly", "Annabelle", "Rosie"]

names * 2

"Jeanne" in names
"Leslie" not in names



