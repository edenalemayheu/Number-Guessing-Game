import random

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100")

number = random.randint(1, 100)
tries = 0

while True:

    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a number only.")
        continue

    guess = int(guess)
    tries += 1

    if guess == number:
        print("You guessed the number!")
        print("Total tries:", tries)
        break

    elif guess < number:
        print("Too low.")

    else:
        print("Too high.")