#lists in python
#list are mutable, ordered collections of items that can be of different data types.
# They are defined using square brackets [] and can be modified after creation.
my_list = [1, 2, 3, "apple", "banana"]
# Accessing elements: using indexing
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # 'apple'
print(my_list[1])  # 'banana'
print(my_list[2])  # 'cherry'
# Negative indexing: accessing elements from the end
print(my_list[-1])  # 'cherry'
print(my_list[-2])  # 'banana'
print(my_list[-3])  # 'apple'
#modifyiing lists 
#.appending elements: using append() method
my_list.append("orange")
print(my_list)  # ['apple', 'banana', 'cherry', 'orange']
# Inserting elements: using insert() method
my_list.insert(1, "kiwi")
print(my_list)  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']
# Removing elements: using remove() method
my_list.remove("banana")
print(my_list)  # ['apple', 'kiwi', 'cherry', 'orange']
# Popping elements: using pop() method
popped_item = my_list.pop()  # removes and returns the last item
print(popped_item)  # 'orange'
print(my_list)  # ['apple', 'kiwi', 'cherry']
# deleting elements: using del statement .pop() method
del my_list[1]  # removes the item at index 1
print(my_list)  # ['apple', 'cherry']
# Clearing the list: using clear() method
my_list.clear()
print(my_list)  # []    
#slicing lists: accessing sublists using slicing
my_list = ["apple", "banana", "cherry", "orange", "kiwi"]
subset = my_list[1:3]  # ['banana', 'cherry']
print(my_list[1:4])  # ['banana', 'cherry', 'orange']
print(my_list[:3])  # ['apple', 'banana', 'cherry']

#list manipulation methods: using various list methods
my_list = ["apple", "banana", "cherry", "date"]
print(my_list[0]) # 'apple'
print(my_list[3]) # 'date'
#add and insert items
my_list.append("elderberry")
print(my_list)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']
my_list.insert(2, "fig")
print(my_list)  # ['apple', 'banana', 'fig', 'cherry', 'date', 'elderberry']
#remove items
my_list.remove("banana")
print(my_list)  # ['apple', 'fig', 'cherry', 'date', 'elderberry']
#delete items
del my_list[0] # removes the first item
print(my_list)  # ['fig', 'cherry', 'date', 'elderberry

#list Functions and Methods: 
# using built-in functions and methods for list operations
len([1,2,3,4]) # 4 (length of the list)
#min() and max(): finding minimum and maximum values
min([5,3,8])    # 3 (minimum value)
max([5,3,8])    # 8 (maximum value)

#common list methods: 
# using methods like sort(), reverse(), count(), extend()
my_list = [3, 1, 4, 2]
my_list.sort()  # sorts the list in ascending order
print(my_list)  # [1, 2, 3, 4]
my_list.reverse()  # reverses the order of the list
print(my_list)  # [4, 3, 2, 1]
print(my_list.count(3))  # 1 (counts occurrences of 3)
my_list.extend([5, 6])  # extends the list with another list
print(my_list)  # [4, 3, 2, 1, 5, 6]    

#Nesting Lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a nested list
print(matrix[0][0])  # 1 (first row, first column)
print(matrix[1][2])  # 6 (second row, third column)
# Modifying elements in a nested list
matrix[0][1] = 10
print(matrix)  # [[1, 10, 3], [4, 5, 6], [7, 8, 9]]

#final challehge: create a programm that asks the user for their top 3 favorite books and stores them in a list, andprints the list in a sorted order.
favorite_books = []
for i in range(3):
    book = input(f"Enter your favorite book {i + 1}: ")
    favorite_books.append(book)
favorite_books.sort()
print("Your favorite books in sorted order:")
for book in favorite_books:
    print(book) 
    