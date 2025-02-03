#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = 100
ounces = grams_to_ounces(grams)
print(f"{grams} грамм = {ounces} унция.") 
#3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return int(y), int(x)

numheads = 35
numlegs = 94
y, x = solve(numheads, numlegs)
print(f"{y} rabbits : {x} chickens ")
 
#4
def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 3 or num == 2:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num**0.5) + 1, 6):
            if num % i==0 or num % (i+2) ==0:
                return False 
        return True
    
    return [num for num in numbers if is_prime(num)]

numbers=[2,3,4,5,6,7,8,12,15,83,]
primes = filter_prime(numbers)
print("jai sandar:", primes)       

#6
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