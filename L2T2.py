#Level 2 Task 2

import random
number = random.randint(50, 150)
nguesses = 0
print("Guess the number between 50 to 150")
while True:
    guess = int(input("Guess the number : "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Congratulations")
        print("You guessed it in ",nguesses," attempts")
        break
    nguesses += 1
