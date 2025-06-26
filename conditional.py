#conditional logic in python
weather = "sunny"
sunny = weather == "sunny"
if (sunny):
    print("Take an umbrella")
else:
    print("Wear sunglasses")
    
# syntax of python conditional statements: uses inndentation and condition is evaluated as True or False
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    
#comparison & logical operators
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
age = 20
is_student = True
if age >= 18 and is_student:
    print("Eligible for student discount")
else:
    print("Not eligible for student discount")