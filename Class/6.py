import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 17, 18, 23, 31, 50]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)