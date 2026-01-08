"""
loops in python

A for loop in python is a control structure the lets you repeat a block of code for each item in sequence such as (list, string, tuple, dictionary or range of numbers)

for variable in sequence:
      - code block runs for each item in the sequence 

"""
# Example 
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("----------") 

for letter in "Lemuel":
    print(letter)

print("---------")

for number in range(5): # 0 to 4 range only includes number less the the stop value 
  print(number)

for number in range(2, 10): #starts at 2 and stops before the 10
  print(number)

print("------------")  

for number in range(0,10, 2): # starts at 0 ends before 10, step by 2 
    print(number)

"""
#mini challenge

1. ask user to enter a number and store it in a variable called num
2. use a for loop with range (1,111) to repeat 10 times from (1,10)
3. inside the loop, multipy num by the current loop value 

"""
print("-------------")
print("--Mini Challenge---")

num = int(input("Enter a number:" ))

for x in range(1, 11):
   print( f"{num} * {x} = {num * x}")


"""
While loops repeats a block of code as long as a condition is True.

While condition
 - code block runs as long as conditionis true 

"""
print("------------------------------------")
count = 1

while count <=5:
    print("count is: ", count)
    count += 1 # increase count by 1


number = 0

while True: #infinite loop
  print(number)
  number +=1
   if number == 23:
       break # exit the loop when number is 23