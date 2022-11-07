# Dictionaries in Python are containers that store key:value pairs!
# keys in a dictionary must be unique! cannot contain duplicates!
# values can be any objects and can contain duplicates!
# dictionaries are mutable and ordered!
# each key has a dedicated value paired to it. this will not change unless changed!
# i.e we can extract values by specifying the key
# but the sequence of keys inside a dictionary does not follow an order!
# can shuffle automatically! but a key will ultimately remain paired to its value!
# meaning that key:value pairs are unordered inside a dictionary!!

ages = {"James":26, "Nathan":19, "Natalie":25, "Jimmy":33, "Pamela":29}
type(ages)

ages["Pamela"] # key based indexing!
ages["Nathan"]
ages.get("Nathan") # 19

# adding new key:value pairs!
ages["Samantha"] = 25
ages # {'James': 26, 'Nathan': 19, 'Natalie': 25, 'Jimmy': 33, 'Pamela': 29, 'Samantha': 25}

# deleting a key:value pair!
del ages["Pamela"]
ages
ages.pop("Nathan")
ages

# mutating dictionary values
ages["Jimmy"] # 33
ages["Jimmy"] = 34
ages["Jimmy"] # 34

# removing all contents of a dictionary
ages
ages.clear()
ages # empty dict!

pairs = {"Nathan":"Julia", "James":"Janice", "John":"Nicky", "Sam":"Christina"}
pairs.keys()
pairs.values()
pairs.items()
for x,y in pairs.items():
    print(x,y)

def count(container):
    """Enumerates the unique elements in a container
    and returns their frequencies as a Python dictionary!"""
    container = list(container)
    counts = dict()
    for i in container:
        if i not in counts.keys():
            counts[i]=1
        elif i in counts.keys():
            counts[i]+=1
    return counts

peers = ["Kye","Penolope","Kye","Julie","julie","Demi","Flora","Flora","Amelia","Jennifer","Claudia","amelia"]
count(peers)
count(list(range(0,200,2))+list(range(50,250,4))+list(range(1,200,5)))