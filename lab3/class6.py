
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 18, 19]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)
