#Defining and calling functions
#def()
def greet():
    print("Hello, welcome to the program!")
greet()

#parameters and arguments
#parameters: Variables defined in the function declaration
#arguments: Values passed to the function when called
def greet(name): #name is a parameter
    print(f"Hello, {name}!")
greet("Alice") # "Alice" is an argument

#engage &m apply: Create a finction to introsuce yourself
def introduce(name, age, hobby):
    print(f"Hello, my name is {name}. I am {age} years old and I enjoy {hobby}.")
introduce("Bob", 25, "painting")

#return statement: using the rerturn keyword, it returns that value, and no longer executes the code after it
def add_numeber(a, b):
    return a + b  # Returns the sum of a and b
result = add_numeber(5, 3)
print(f"The sum is: {result}")

#Function Scope(Local and Global Variables)
#Local variables: Defined within a function and can only be accessed within that function
def local_variable_example():
    local_var = "I am a local variable"
    print(local_var)
local_variable_example()
#Global variables: Defined outside any function and can be accessed anywhere in the code
global_var = "I am a global variable"
def global_variable_example():
    print(global_var)
global_variable_example()

#default parameters & variable-length arguments
#Default parameters: Parameters that have a default value if no argument is provided
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")
greet_with_default()  # Uses default value
greet_with_default("Charlie")  # Uses provided value    
#Variable-length arguments: Allows a function to accept any number of arguments
def variable_length_args(*args):
    for arg in args:
        print(arg)
variable_length_args("apple", "banana", "cherry")  # Accepts multiple arguments 

#final challenge: create a function that takes a list of numbers as an argument, squares each number, and returns a new list with the squared values.
number = [3, 99, 12, 1, 7]  
def square_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers  
squared_list = square_numbers(number)
print(f"The squared numbers are: {squared_list}")
