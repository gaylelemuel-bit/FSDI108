"""
Functons

A fucntioc is a block of code that only runs when it is called
we can pass data to finctions (parameters). and they can return data as resutlt

def function_name(parameters):
    -code block (indeed)
    -return value # optional 
"""

def my_function():
    print("this is a function")

my_function() # calling the function

def greet():
    print("wassup!")

greet()

def get_full_name():
    first_name = "Lemuel"
    last_name = "Gayle"
    full_name = first_name + " " + last_name
    return full_name
print(get_full_name())
print("--------------")

def my_fullname(first_name, last_name):
    return f"hello {first_name} {last_name}" # return full name

    my_name = my_full_name("Lemuel", "Gayle")
    print(my_name)

