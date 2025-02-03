from my_functions import grams_to_ounces,solve,filter_prime,guess_the_number

grams = 100
print(f"{grams} грамм = унция. :{grams_to_ounces(grams)}")

numheads = 35
numlegs = 94
print(f" chickens :{solve(numheads, numlegs)}")
 
numbers=[2,3,4,5,6,7,8,12,15,83,]
print(f"jai sandar: { filter_prime(numbers)}")

play = input("Do you want to play 'Guess the Number'? (yes/no): ")
if play.lower() == "yes":
    guess_the_number()