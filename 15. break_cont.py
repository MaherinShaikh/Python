# break statement is used to exit a loop prematurely when a certain condition is met. It can be used in both for and while loops. When the break statement is executed, the loop is immediately terminated and the program continues with the next statement after the loop.

for i in range (1, 13):
    print("5 X ", i, "=", 5*i)
    if i == 10:
        break     #iss loop ko chodke nikal jaao

print("Loop exited at i =", i)

# continue statement is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds with the next iteration.

for i in range (1, 13):
    if i == 10:
        print("Skipping iteration for i =", i)
        continue   #iss loop ko skip kar do, aur next iteration pe jao
    print("5 X ", i, "=", 5*i)