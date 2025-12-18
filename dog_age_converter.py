print("--- Dog Age Converter --")

# wrapped in "int" to perfom the math operatoin
dog_age = int(input("What is your dog's age in human years?: " ))
dog_name = " Leonard Brisket Anothony jr."

# mult line f-string with triple quotes

print(f"""
{dog_name} is {dog_age * 7} years old in dog years!
Cherish these moments with him. 
 =)
""") 