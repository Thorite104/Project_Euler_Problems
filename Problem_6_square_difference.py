#The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def square_of_sum(n):
    sum1 = 0.5*(n*(n+1))
    sqr = sum1 ** 2
    return int(sqr)

def sum_of_square(n):
    sum2 = (1/6)*n*(n+1)*((2*n)+1)
    return math.ceil(sum2)

print (sum_of_square(100))
print (sum_of_square(100) - square_of_sum(100))