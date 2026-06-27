# conditional operators
# >, < , >=, <=, >=, ==, !
a = int(input("Enter your age: "))
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

# conditional statements
# if else
if a<18:
    print("you cannot drive")
else:
    print("you can drive")

print("This will always be printed as it is out of conditional statements")

# elif statement
if a<18:
    print("you cannot drive")
elif a==18:
    print("you can drive but be careful")
else:
    print("you can drive")
