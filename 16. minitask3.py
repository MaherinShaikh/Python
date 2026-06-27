#Number Guessing Game

# secret = 10

import random
secret = random.randint(1, 20)

for i in range(1, 6):  # This loop will run for 5 attempts
    print("Attempt no.", i)
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Congratulations! You guessed the number in", i, "attempts.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print("Game over! The secret number was", secret)