# List in python

"""
A list is a built-in data structure in python used to store multiple items in a single variable.
lists are order, mutable, and allow duplicated values.

variable_name =[item1, item2, item3,....]
"""

# Creating Lists
my_list =[10, 20, 30, 40]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing Items ... using the indexs
fruits = ["apple", "banana", "cherry"] 
print(fruits[0]) # print out apple
print(fruits[1]) # print out banana
print(fruits[2]) # print out cherry 

print(fruits[-1])# -1 prints out the last item in your list 
print(fruits[-2])# prints out the second to last item 

# Slicing list
print(fruits[0:2]) #prints all items from 0 and stops at 2"does include the "
print(fruits[:2]) # first two elements 
print(fruits[1:])# starts at 1 and goes to end of index 

# Modifying lists
fruits[1]= "mango" # replace banana with mango 
print(fruits)

# Adding items 

fruits.append("orange") 
print(fruits)

fruits.insert(1, "kiwi")# inserts at index 1
print(fruits)

# Removing items
fruits.remove("apple") # remove by the value 
print(fruits)

fruits.pop() # removes the last item
print(fruits)

del fruits[0] # removes item at index 0
print(fruits)

# List length
print(len(fruits))
print(len(["cohort63", True, False, "python", 3.14545, 2025]))

"""
Mini challenge: Favorite movies 
create a list of 4 favorite movies 
replace the second movie with a new one 
step 3 remove one movie 
option a: remove by value
option b: remove by index
"""

favorite_movies=["training day", "300", "up", "superman"]
print(favorite_movies)

favorite_movies[1]="yes day" # adds new movie

del favorite_movies[0]
print(favorite_movies)


# Assignment 2
print(" ---------- Assignmet #2 ---------- ")
bible_list = ["Ecclesiastes", "John","Deuteronomy","Exodus", "Proverbs"]
print(bible_list)
print(bible_list[0])
bible_list[3]= "James"
print(bible_list)
del bible_list[2]
print(bible_list)
print(len(bible_list))
