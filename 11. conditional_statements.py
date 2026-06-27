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
<<<<<<< HEAD
=======

# elif acts as else if statement, it is used to check multiple conditions. It is optional, you can use as many elif statements as you want. But you can only use one else statement. The else statement is used to execute a block of code when all the conditions are false.

if a<18:
    print("you cannot drive")
elif a==18:
    print("you can drive but be careful")   
else:
    print("you can drive")


# cleaned up version
wt = int(input("Enter your weight in kg: "))
ht = float(input("Enter your height in metres: "))

bmi = round(wt / (ht ** 2), 1)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")


# nested if else statements
age = int(input("Enter your age: "))
weekend = input("Is it weekend? (yes/no): ")
if age < 12:
    if weekend == "yes":
        print("Ticket price is 100")
    else:
        print("Ticket price is 70")

elif age <= 59:
    if weekend == "yes":
        print("Ticket price is 200")
    else:
        print("Ticket price is 150")

else:
    if weekend == "yes":
        print("Ticket price is 100")
    else:
        print("Ticket price is 80")

print("YAYYY!!!")
>>>>>>> 69fe127 (nested if-else example)
