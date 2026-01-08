"""
if-else statements in python

an if-else statement in python is a conditional structure that lets you decide which block of code to run depending onwether a condition is True or False.

the if block runs only if the condidtionevaluates to True.
If the condition is False, the else block runs instead.
you can also add elif(else if blocks to check multiple conditions.)

if condition:
    # code to execute if condition is True
elif:
    - code block runs if firstcondition is flase and this condition is True
else:
    - code block runs if none of the above conditions are True

"""
# Examples

x = 23

if x > 23:
    print("x is greater than 23")
elif x == 23:
    print("x is equal to 23")
else:
    print("x is less than 23")
"""
 # Nest if Statements
 if x > 0:
    if x < 20:
        print("x is a positive number less than 20") 
   
   # combine conditions
   if age >=18 and age <=21:
    print("you are between 18 and 21") 

    username= "john123"
     if username == "peter321":
        print("you are peter!")
"""

"""
# Mini Challenge
1.ask the user to enter a number from 0-100 and store in dthe varabile called "score"
2.the score is under 90 or above, print "Grade: A"
3. if the score is between  80-90, prnt "Grade: B"
4. if the score is between 70-90, print " Grades:C"
5. otherwise, print " Grade:F"
"""

score = int(input("enter a number from (0-100): "))

if score >=90:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 60 and score <= 79:
    print("Grade C")
else: 
    print("Grade F")

""" 
#Mini Challenge
1.ask user to enter temp i fahrenheit and store in variable called temperature
2.use if-else-elif statements to classify the temperature
if tempature >= 86, print " its hot outside!"
if temperature >= 68 and temperature < 86, print "the weather is nice"
if temparature is >=50 and temperature < 68, print "its's a bit chilly"
otherwise, print "its's cold!"
"""
temperature =float(input("what is todays temperature in fahernheit? "))

if temperature >= 86:
    print("Its hot outside!")
elif temperature >= 68 and temperature <=85:
    print("the weather is nice")
else:
    print("its cold!")