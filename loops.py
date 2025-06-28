#For and While Loops
#for item in iterable - code blocks to be executed

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
# while condition - code blocks to be executed
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  
# range(start, stop, step) - generates a sequence of numbers
for i in range(1, 10, 2):
    print(i)    
    
# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")    
        
#Write a pyrhon program that prints all even numbers from 1 to 20 usinf a while loop
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1    

#Control Flow Statements break, continue, pass
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
for i in range(1, 11):
    if i == 5:
        continue  # Skip the iteration when i is 5
    print(i)
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing when i is 5, but continue the loop
    print(i)

#Final Challenge: write a programm that processes numbers from 1 to 30.
# If a number is divisible by 3, print a message.
# If a number is greater than 25, break the loop.    

for i in range(1, 31):
    if i % 3 == 0:
        continue
    if i > 25:
        break
    else:   
        print(f"Processing number: {i}")