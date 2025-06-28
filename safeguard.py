#safeguarding your code - python exceptions
# Exceptions are errors that occur during the execution of a program.
# They can be handled using try-except blocks to prevent the program from crashing.

#exceptions
#comnmon exceptions in python
# - ZeroDivisionError: Raised when dividing by zero.
# - IndexError: Raised when trying to access an index that is out of range in a list or tuple.
# - KeyError: Raised when trying to access a dictionary key that does not exist.
# - ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
# - TypeError: Raised when an operation or function is applied to an object of
# Syntax Error
#if True
  #  print("Hello")  # Missing colon at the end of if statement

# Runtime Exception
#x = 1 / 0  # This will raise ZeroDivisionError
# try:
#     # Code that may raise an exception
#     result = 10 / 0  # This will raise a ZeroDivisionError
#try:
    # Code that may raise an exception
#except ExceptionType:
    # Code that runs if an exception occurs
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")  
#try:
#    x = 10 / 0
#except ZeroDivisionError:
#    print("You can't divide by zero!")
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
    
#Catching Multiple Exceptions in One Block:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
#Catching Any Exception in One Block:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except:
    print(f"An error occurred!")

#else and finally Clauses:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is: {result}")
finally:
    print("This block always runs, regardless of whether an exception occurred or not.")

