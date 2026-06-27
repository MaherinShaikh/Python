# ordered collection of items
# multiple items in single variable
# seperated by commas and enclosed in square brackets
# lists are changeable, meaning you can modify their contents after creation. You can add, remove, or change elements in a list. Lists can contain elements of different data types, including other lists, making them versatile for various applications.

marks = [1, 2, 3, 4, 5]
print(marks)
print(marks[:])
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

name = ["john", "doe", "smith"]
print(name)

details = ["john", 25, 5.9, True]  # can have different data types
print(details)

#Negative indexing in lists allows you to access elements from the end of the list. The last element has an index of -1, the second-to-last element has an index of -2, and so on. This feature is useful when you want to retrieve elements relative to the end of the list without knowing its length.

colors = ["red", "green", "blue", "yellow"]
print(colors[-1])  # Output: yellow
print(colors[len(colors)-3])  # Output: green
print(colors[4-2])  # Output: blue
print(colors[0])  # Output: red


#check whether an item exists in a list using the in keyword. This allows you to determine if a specific value is present in the list, returning True if it is found and False otherwise.
if "green" in colors:
    print("green is present in the list")
else:
    print("green is not present in the list")

if "en" in colors:
    print("en is present in the list")
else:
    print("en is not present in the list")

# if "re" in red:
#     print("ed is present in the list")

#jump index
print(colors[0:3])  # Output: ['red', 'green', 'blue']
print(colors[0:4:2])  # Output: ['red', 'blue'] 

#list comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering the items based on a condition. List comprehensions are often more readable and efficient than using traditional loops for creating lists.

lst = [i*i for i in range(10)]  # This will create a list of numbers from 0 to 9
print(lst)

lst = [i*i for i in range(10) if i % 2 == 0]  # This will create a list of even numbers from 0 to 9
print(lst)
