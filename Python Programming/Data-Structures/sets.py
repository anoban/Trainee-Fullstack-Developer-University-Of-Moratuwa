# Python sets
# a container
# no duplicates are allowed!
# all elements must be unique
# when another container data type is type casted to sets, duplicates will automatically be removed.
# elements in a set are not indexed in Python!!

names = {"John", "Samson", "Kevin", "Jamil", "Nathan", "Janice"}
type(names)     # <class 'set'>

names = {"John", "Samson", "Kevin", "Jamil", "Nathan", "Janice", "Nathan", "Lesile", "Grace", "Nathan", "Kevin"}
names       # {'Grace', 'Nathan', 'Lesile', 'Janice', 'Samson', 'Jamil', 'Kevin', 'John'}
# duplicates are removed automatically!!!

names = set(["John", "Julia", "Samantha", "Sonia", "Alice", "Kevin", "Samson", "Kevin", "Jamil", "Nathan", "Janice", "Nathan", "Lesile", "Grace", "Nathan", "Kevin"])
names       # {'Alice', 'Sonia', 'Grace', 'Nathan', 'Lesile', 'Samantha', 'Julia', 'Janice', 'Samson', 'Jamil', 'Kevin', 'John'}

fruits = set(["Apple", "Watermelon", "Orange", "Pear", "Cherry", "Strawberry", "Nectarine", "Grape", "Mango", "Blueberry", "Pomegranate", "Carambola", "Starfruit", "Plum", "Banana", "Raspberry", "Mandarin", "Jackfruit", "Papaya", "Kiwi", "Pineapple", "Lime", "Lemon", "Apricot", "Grapefruit", "Melon", "Coconut", "Avocado"])

# to add a single element
fruits.add("Mangosteen")
fruits

# to add a series of elements
fruits.update(["Dates", "Blackberry","Pineapple"])
fruits

# to sort the elements alphabetically
sorted(fruits)

# to remove an arbitrary element
fruits.pop()        # 'Avocado' has gone!

# to remove an element; will raise an error if the requested element is absent in the set
fruits.remove("Dates")
sorted(fruits)      # Dates is gone!
fruits.remove("Hahah")      # KeyError

# to remove an element; won't raise an error if the required element does not exist in the container!
fruits.discard("Pineapple")
sorted(fruits)
fruits.discard("hahaha")        # Nothing happened!

len(fruits) # 29


# set operations!

odds = set([1,3,5,7,9,11,13,15])
evens = set([2,4,6,8,10,12,14])

odds | evens # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
odds.union(evens)
evens.union(odds)
odds.union(evens) == evens.union(odds) # true!

odds.intersection(evens)  # empty set!
set([1,2,3,4,5,6,7]).intersection(set([4,5,6,7,8,9,10,11,12]))
# {4, 5, 6, 7}
set([4,5,6,7,8,9,10,11,12]).intersection(set([1,2,3,4,5,6,7]))
set([1,2,3,4,5,6,7]).intersection(set([4,5,6,7,8,9,10,11,12])) == set([4,5,6,7,8,9,10,11,12]).intersection(set([1,2,3,4,5,6,7]))
# true!

nums_1 = set(list(range(1,30,5)))
nums_2 = set(list(range(20,100)))
nums_1.union(nums_2)
nums_1 | nums_2
nums_1.intersection(nums_2)
nums_1 & nums_2

# set_1.union(set_2) = set_1 | set_2
# set_1.intersection(set_2) = set_1 & set_2

# this method will not produce identicals results when applied vice versa!!!!!!
nums_1.difference(nums_2)
nums_1 - nums_2
nums_2.difference(nums_1)
nums_2 - nums_1