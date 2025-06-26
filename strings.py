#string single quotes
string_single_quotes = 'Hello, World!'
#string double quotes
string_double_quotes = "Hello, World!"
#string multiline triple quotes
string_multiline_triple_quotes = """Hello,
World!"""
#string indexing
string_indexing = string_single_quotes[0]  # 'H'

#String Operations: thsese operations are fundamental for manipulating strings in Python.

#string slicing
string_slicing = string_single_quotes[0:5]  # 'Hello'
#string concatenation: combined + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # 'John Doe'
#string repetition: using * operator
exclamation = "Wow! " * 3  # 'Wow! Wow! Wow! '
#string length: using len() to fing length
name = "Python" 
print(len(name))  # 6 
#accessing substrings: using slicing
language = "JavaScript"
print(language[0:4])  # 'Java'
print(language[4:10])  # 'Script'
print(language[-6:])  # 'Script'

#String Methods: these methods are essental tools for prosessing and manipulating text data effeciently in Python.

#string methods: using methods like str.upper(), str.lower()
message = "Hello, World!"
print(message.upper())  # 'HELLO, WORLD!'
print(message.lower())  # 'hello, world!'
#string find: using str.strip(), str.find()
text = "   Hello, World!   "
print(text.strip())  # 'Hello, World!'
print(text.find("World"))  # 8
#string replace: using str.replace()
message = "Hello, World!"
print(message.replace("World", "Python"))  # 'Hello, Python!'
#string split: using str.split()
sentence = "Python is great"
words = sentence.split()  # ['Python', 'is', 'great']
#string join: using str.join()
words_list = ['Python', 'is', 'great']
joined_string = " ".join(words_list)  # 'Python is great'
#str.startswith() and str.endswith()
filename = "report.pdf"
print(filename.startswith(("report.pdf")))  # True
print(filename.endswith(".pdf"))  # True 

#String Formatting: these techniques are essential for creating dynamic and readable strings in Python.

#str.format() method: using str.format() for formatting strings
name = "James"
age = 30
print('My name is {} and I am {} years old.'.format(name, age))  # 'My name is James and I am 30 years old.'
#f-strings (Python 3.6+): using f-strings for formatting strings
name = "Alice"
age = 25
print(f'My name is {name} and I am {age} years old.')
#% formatting: using % operator for formatting strings
name = "Bob"
age = 40
print('My name is %s and I am %d years old.' % (name, age))  # 'My name is Bob and I am 40 years old.'

#String pitfallss and tips

#immutable strings: strings are immutable, meaning they cannot be changed after creation
text = "Hello"
# text[0] = 'h'  # This will raise a TypeError
# Instead, create a new string
new_text = 'h' + text[1:]  # 'hello'
#concatenation in loops: Using +- 
result = ""
result += "a" #the same thing would be result = result + "a"

#Final Challange: build text-based name generator that combines random first and last names.

first_names = ["John", "Jane", "Alice", "Bob"]
last_names = ["Doe", "Smith", "Johnson", "Brown"]
import random
random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)
print(f"Random Name: {random_first_name} {random_last_name}")