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

#commin pitfalls & tips


# Pitfall: all conditions are checked 
if x > 0: 
		print("Positive") 
if x == 0: 
		print("Zero") 
else: 
		print("Negative") 

# Correct approach using elif 
if x > 0: 
		print("Positive") 
elif x == 0: 
		print("Zero") 
else: 
		print("Negative")
  
bootcamp = 'coding temple'

# Incorrect Way:
#if (bootcamp = 'coding temple'): # would throw an error
		#print('best bootcamp ever!')

# Correct Way:
if (bootcamp == 'coding temple'):
		print('best bootcamp ever!')
  
#final challenge: create a program where the user has to guess a number between 1 and 10.
import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print("Congratulations! You guessed the number.")
elif guess < secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")   