#python basics Sess-1

print("whadddup doh?!!!")
print(3)
print(2+8)

print("Cohort#63welcome")
"""
mult line code here
triple quotes let you write longer explanations 
"""

# -- varibles and conatention --
name="Lemuel"
age= 30
print(name) # prints variable value

print("my name is "+ name + " and i am " + str(age)+ " years old")

first_name = "Michael"
middle_name = "phillip"
last_name = "Jordan"
age= 53 
print("My name is " + first_name + " " + middle_name + " " + last_name + " and I am " + str(age) + " year old.")


# --- F-String (cleaner way to write strings)
print(f"hello")
print(f"my name is {first_name} {middle_name} {last_name} and I am {age} years old!")

#mult line f-string
print(f"""
my name is {first_name} {middle_name} {last_name} and I am {age} years old.
""")


"""
-create 4 variable :my_name, my_last_name,my_age, and my_favorite_technolgy.
-assign thme your own info 
the, use f-string to print a sentence below example 
"hello my name is _ _, I am _ years old and my favorite technology is _."

personalize the valies with real data
you can also add extra data like city or hobby
"""

my_name = "Lemuel"
my_last_name = "Gayle"
my_age = 30
my_favorite_technolgy ="Python"
my_hobby ="eating"
my_hobby2 ="traveling"
my_hobby3 ="workingout"
my_city ="Dallas"

print(f"""
Hello! my name is {my_name} {my_last_name} I am big {my_age} years old. 
I live in {my_city}, some of the favorite hobbies are {my_hobby}, {my_hobby2} and {my_hobby3}. 
My favorite technology is {my_favorite_technolgy}.
""")

#type function 
print(type("peter"))
print(type(last_name))
print(type(True))
print(type(34526))
print(type(99.9))

# -- Input Fucntion --

user_name = input("Enter your name: ")
print(f"Hello {user_name}")

user_age = int(input("enter your age: "))
print(f"You are {user_age - 1} years old!")