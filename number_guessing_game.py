import random

print("🎲 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

# Generate a random number
number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < number:
            print("🔻 Too low! Try again.")
        elif guess > number:
            print("🔺 Too high! Try again.")
        else:
            print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("⚠️ Please enter a valid number.")