"""
Tuples in Python
A tuple is a buit-in data structure in python like a list.
tuples can store muiltpie items, but they are immutable.

my-tuple =(item1, item2,item3,..)

"""

my_tuple = ("Mango", "strawberry", "Pineapple")
print(my_tuple)

print(my_tuple[0])

#length
print(len(my_tuple))

#single_item tuple
single = ("apple")

# tuple has a , at the end 
corect =("apple,")

print(my_tuple[0:2])# prints first and second, ends at 2

# Nest tuples
tuple1 =("a", "b", "c")
tuple2 =(1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

temp_list = list(my_tuple) # converts to list 
print(temp_list)

temp_list.append("Kiwi")
my_tuple = tuple(temp_list) # converts back to tuple
print(my_tuple)

"""
Mini Challenge
1.creat a tuple called travel_bag with at least 5 items: "shirt", "pants", "toothbrush", "shoes" "socks" "deoderant"
2. print the second and fourth items in the tuple
make a newtuple called essentials wiyh 3 must-have items "passport", "money", "keys"

"""
travel_bag = ("shirt", "pants", "toothbrush", "shoes", "socks", "deoderant")
print("-- Mini Challenge --")
print(travel_bag)
print(travel_bag[1])
print(travel_bag[3])

essentials = ("passport", "money", "keys")
print(essentials)