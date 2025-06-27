print ("This is the project.py file")

print ("TThe changes made in the project.py file will be reflected in the main.py file")


#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Test the function
print(even_or_odd(2))  # Output: "Even"
print(even_or_odd(1))  # Output: "Odd"

#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know? (input --> output):
#123  --> "123"
#999  --> "999"
#-100 --> "-100"

def number_to_string(num):
    return str(num)

# Examples
print(number_to_string(123))   # "123"
print(number_to_string(999))   # "999"
print(number_to_string(-100))  # "-100"

#Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

#Write a function that removes the spaces from the string, then return the resultant string.

#Examples (Input -> Output):

#"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
#"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
#8aaaaa dddd r     " -> "8aaaaaddddr"
def no_space(x):
    return x.replace(" ", "")   
# Examples
print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))  # "8j8mBliB8gimjB8B8jlB"
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))  # "88Bifk8hB8BB8BBBB888chl8BhBfd"
print(no_space("8aaaaa dddd r     "))  # "8aaaaaddddr"  