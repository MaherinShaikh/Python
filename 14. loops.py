# for loop
name = "john"
for i in name:
    print(i)
    if i == "o":
        print("found o")


colors = ["red", "green", "blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# range function
for i in range(5):
    print(i + 1)

for i in range(1, 10, 2): 
#   this will print odd numbers from 1 to 9 start stop step
    print(i)

# while loop 
x = 0
while x < 5:
    print(x)
    x = x + 1

i = int(input("Enter a number: "))
while i <=20:
    print("You entered a number less than or equal to 20")
    i = int(input("Enter a number: "))
    print(i)

print("out of loop")

# decrementing loop 
i = 5
while i > 0:
    print(i)
    i = i - 1
else:
    print("Loop ended")   #while loop with else statement, the else block will be executed when the loop is finished, but not when the loop is terminated by a break statement.

#emulate do while loop in python
# Python does not have a built-in do-while loop like some other programming languages. However, you can achieve similar functionality using a while loop. The key difference between a do-while loop and a while loop is that a do-while loop guarantees that the loop body will be executed at least once, while a while loop may not execute at all if the condition is false from the beginning.

i = 0
while True:  # This creates an infinite loop
    print(i)
    i = i + 1
    if i % 100 == 0:  
        break
