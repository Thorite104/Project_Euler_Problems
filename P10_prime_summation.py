#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#My Solution
import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


sum = 0
start = 1

while start <= 2000000:
    if isPrime(start) == True:
        sum += start
    start += 1

print (sum)

