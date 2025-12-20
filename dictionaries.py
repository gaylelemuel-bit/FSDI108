# Dictionaries in python

"""
A ldictionary is a built-in data structure in python used to store in key:value pairs.
Dictionaries are mutable, ordered, keys must be unique.

#opt 1
variable_name ={"key1": value1, "key2": value2....}

opt2
my_variable = {
    "key1": value1,
    "key2": value2,
    ...
}
"""
# Creating  a dictinary
student = {
    "name": "lemuel",
    "age": 28,
    "major":"computer science"
}
print(student)

new_student={
    "name":"pam",
    "age":32,
    "name":"mike"# if you use same key twice, the vlast value overrides it 
}
print(new_student)

# Accessing Items
print(student["name"])
print(student["age"])

# Adding new items to dictionary 
student["graduation_year"]= 2025
print(student)

#change value
student["age"]=20
print(student)

#remove items 
student.pop("major") # removes by key 
print(student)

del student["name"] # removes specfic key 
print(student)

# Dictionary length
print(len(student))

# Clearing Dictionaries
student.clear()
print(student)

student_group ={
    "student_one":{
        "name":"moses",
        "age": 120,
    },
    "student_two":{
        "name":"jesus",
        "age": 30,
    }
}
print(student_group)
print(student_group["student_two"],["name"])

"""
---Mini Challenge
create dictionary title,artist,duration
print title
add a new key "ablum
"""

songs_list ={
    "song_one":{
        "title":"Bandit",
        "artist":"Caleb Gordon",
        "duation":2.30,
    },
     "song_two":{
        "title":"war",
        "artist":"Caleb Gordon",
        "duation":3.30,
    },
     "song_two":{
        "title":"I need peace",
        "artist":"Caleb Gordon",
        "duation":3.10,
    },
}
print(songs_list)
print(songs_list["song_one"],["title"])

# Assignment 2
print(" ---------- Assignmet #2 ---------- ")
characters ={
    "name": "Moses",
    "age": 95,
    "book": "Exodus",
    "wrote": 4,
    "status": "married",
    "children": True
}
print(characters)
print(characters["status"])
characters["mission"]= "Save Israel"
print(characters)
characters["age"]= 120
print(characters)
del characters["mission"]
print(characters)
print(len(characters))