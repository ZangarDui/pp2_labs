import random

def guess_the_number():
    print("Hello! What is your name")
    name = input()

    secret_number = random.randint(1,20)
    print(f"/nWell, {name},I am thinking of a number between 1 and 20")

    attempts = 0 

    while True:
        print("Takes a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses.")
            break
 
guess_the_number()