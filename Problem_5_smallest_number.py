#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#STOLE THE SOLUTION BECAUSE THERE IS AIDS FACTORISATION
#

from math import floor

# A simple function to test whether a number is prime.
def is_prime(n):
    for x in range(2, floor(n ** 0.5) + 1):
        if n % x == 0:
          return False
    return True

# The number we'll check up to. Set to 10 to test the code then change to 20.
limit = 20

# A list of primes we know show up at least once.
primes = [x for x in range(2, limit + 1) if is_prime(x)]

# A simple function to calculate the prime factors of a number.
def prime_factors(n):
    result = {prime: 0 for prime in primes}
    i = 0
    for prime in primes:
        while n % prime == 0:
            result[prime] += 1
            n = n / prime
    return result

# Initialize factors. We know each prime below limit shows up at least once.
factors = {prime: 1 for prime in primes}

# Look at the prime counts for each number in our range and keep the highest.
for x in range(2, limit + 1):
    for prime, count in prime_factors(x).items():
        factors[prime] = max(count, factors[prime])

# Calculate and print the result.
result = 1
for prime, count in factors.items():
    result *= prime ** count

print(result)