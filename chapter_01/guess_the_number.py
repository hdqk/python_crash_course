import random
number = random.randint(0,100)
guess = int(input("Guess a number between 1 and 100:\n"))

while guess != number:
    if guess < 0 or guess > 100:
        print("Please choose a number between 1 and 100.")
        guess = int(input("Guess again:\n"))
    if guess < number:
        print("Too low!")
    if guess > number:
        print("Too high!")
    guess = int(input("Guess again:\n"))
    
if guess == number:
    print(f"Correct! The number I was thinking of is {number}.")

