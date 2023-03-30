import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("\nGuess the number (1-100)\n> "))
    guesses += 1
    
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print(f"Congratulations, you guessed the number in {guesses} guesses!")
        break