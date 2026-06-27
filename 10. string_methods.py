# Strings are immutable mtlb hum change nahi kar sakte. Hum naya string create kar sakte hain but existing string ko change nahi kar sakte.

from curses.ascii import islower

a = "Maherin!!!"
print(len(a))
print(a.upper())
print(a.lower())  # maherin

# rstrip()- trailing characters ko remove karta hai not leading characters
b = "!!!AbcdEF!!!"
print(b)
print(b.rstrip("!"))

# replace()- replaces the string with the new string. It does not change the original string but returns a new string.

print(a.replace("Maherin", "Kashaf"))  # Kashaf
 
# split()- splits the string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.
names = "Maherin,kashaf,reeza"
print(names.split(" "))  # ['Maherin', 'kashaf', 'reeza

# capitalize()- capitalizes the first character of the string and converts the rest to lowercase.
blog = "introduction to python programming"
print(blog.capitalize())  # Python programming

# center()- centers the string within a specified width by padding it with spaces on both sides.
title = "Python Programming"
print(title.center(30))  # '     Python Programming      '

# count()- counts the number of occurrences of a specified substring in the string.
sentence = "Python is a great programming language. Python is widely used."
print(sentence.count("Python"))  # 2

# endwith()- checks if the string ends with a specified suffix. It returns True if the string ends with the suffix, and False otherwise.
filename = "report.pdf" 
print(filename.endswith(".pdf"))  # True

# find()- searches for a specified substring in the string and returns the index of the first occurrence. If the substring is not found, it returns -1.
text = "Hello, welcome to Python programming!"
print(text.find("welcome"))  # 7
print(text.find("Java"))  # -1

# index()- similar to find() but raises a ValueError if the substring is not found.
print(text.index("welcome"))  # 7
# print(text.index("Java"))  # ValueError: substring not found

# isalnum()- checks if all characters in the string are alphanumeric (letters and numbers) and there is at least one character. It returns True if the string is alphanumeric, and False otherwise.
username = "User123"
print(username.isalnum())  # True

# isalpha()- checks if all characters in the string are alphabetic (letters) and there is at least one character. It returns True if the string is alphabetic, and False otherwise.
name = "Maherin"
print(name.isalpha())  # True

# islower()- checks if all characters in the string are lowercase letters and there is at least one character. It returns True if the string is lowercase, and False otherwise.
lowercase_string = "hello"
print(lowercase_string.islower())  # True

# isprintable()- checks if all characters in the string are printable (not including control characters). It returns True if the string is printable, and False otherwise.
printable_string = "Hello, World!"
print(printable_string.isprintable())  # True
non_printable_string = "Hello\nWorld"
print(non_printable_string.isprintable())  # False

# isspace()- checks if all characters in the string are whitespace characters (spaces, tabs, newlines) and there is at least one character. It returns True if the string is whitespace, and False otherwise.
whitespace_string = "   "
print(whitespace_string.isspace())  # True
non_whitespace_string = "Hello"
print(non_whitespace_string.isspace())  # False

# istitle()- checks if the string is in title case, where the first character of each word is uppercase and the rest are lowercase. It returns True if the string is in title case, and False otherwise.
title_string = "Hello World"
print(title_string.istitle())  # True
non_title_string = "hello world"
print(non_title_string.istitle())  # False

# isupper()- checks if all characters in the string are uppercase letters and there is at least one character. It returns True if the string is uppercase, and False otherwise.
uppercase_string = "HELLO"
print(uppercase_string.isupper())  # True
non_uppercase_string = "Hello"
print(non_uppercase_string.isupper())  # False

# startswith()- checks if the string starts with a specified prefix. It returns True if the string starts with the prefix, and False otherwise.
filename = "report.pdf"
print(filename.startswith("report"))  # True
print(filename.startswith("data"))  # False

# swapcase()- converts uppercase letters to lowercase and lowercase letters to uppercase in the string. It returns a new string with the case swapped.
text = "Hello, World!"
print(text.swapcase())  # hELLO, wORLD!

# title()  # converts the first character of each word to uppercase and the rest to lowercase. It returns a new string in title case.
text = "hello, world!"
print(text.title())  # Hello, World!


