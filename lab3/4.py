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