"""
sets in Python

A set is a built-data structure in python used yo store unique items.
sets are unordered, mutable, and do not allow duplicate values.

my_set{item1, item2, item3,..}


"""
fruits = {"mango", "pineapple", "orange", "kiwi"}
print(fruits)

print("mango" in fruits )

fruits.add("banana") # add single item 
print(fruits)

fruits.update(["grapes","watermelon"]) #add multiple items
print(fruits)

fruits.remove("banana") # remove item
print(fruits) 

fruits.discard("kiwi") # remove item without error if not found
print(fruits)

# set operatins

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # Combines both without no duplicates 
print(set1.intersection(set2)) # Common elements
print(set1.difference(set2)) #elements in set1 but not in set2

#length
print(len(set1))

#Copy sets
new_set = set1.copy()
print(new_set)

# clearing sets
set1.clear()
print(set1)