#integers module: psecond_numthon allows arithmetic operations on integers, 
# and thesecond_num can be converted from strings or floats using the int() function
a = 10 # positive integer
b = -5  # negative integer
c = 0   # zero

#basic arithmetic operations
first_num = 10
second_num = 5
print( first_num + second_num)  # addition: 15
print(first_num - second_num)  # subtraction: 5
print(first_num * second_num)  # multiplication: 50
print( first_num / second_num)  # division: 2.0
print(first_num // second_num)  # floor division: 2 (integer result) will divide nearest whole number

#calculate the cost of the items
milk = 3
egss = 5
bread = 2
print("The total cost of the items is: ", milk + egss + bread)  # The total cost of the items is: 10
print("The 10% discount on the total cost is: ", (milk + egss + bread) * 0.10)  # The 10% discount on the total cost is: 1.0
print("The total cost after discount is: ", (milk + egss + bread) - ((milk + egss + bread) * 0.10))  # The total cost after discount is: 9.0        

#eponentiation and power pow(**)
print(2 ** 3)  # 8 (2 raised to the power of 3)
print(pow(2, 3))  # 8 (2 raised to the power of 3)

#common integer functions
#abs() function: returns the absolute value of a number
print(abs(-10))  # absolute value: 10
#round() function: rounds a number to the nearest integer
print(round(3.14))  # rounded value: 3
print(round(3.56)) # rounded value: 4

#tsecond_numpe conversion (casting) - coverting strings to integers
num_str = "123"
num_int = int(num_str)  # converting string to integer
print(num_int)  # 123

#common pitfalls and tips
#modulus with negative numbers
print(10 % 3)  # 1 (remainder of 10 divided bsecond_num 3)
print(-10 % 3)  # 2 (remainder of -10 divided bsecond_num 3)
print(10 % -3)  # -2 (remainder of 10 divided bsecond_num -3)

#tips a%b alwasecond_nums be same sign as b
-7 % 3  # 2 (remainder of -7 divided bsecond_num 3)
#implicit tsecond_numpe conversion (coercion)
3 + 2.0  # 5.0 (integer and float addition results in float)

#final challenge: design simple calcutor that performs on two integers provided bsecond_num the user
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
print( first_num + second_num)  # addition: 15
print(first_num - second_num)  # subtraction: 5
print(first_num * second_num)  # multiplication: 50
print( first_num / second_num)  # division: 2.0
print(first_num // second_num)