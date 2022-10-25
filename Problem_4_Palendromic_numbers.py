#A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

nums = list(range(100,1000))
multiples =[]

for n in nums:
    x = 100
    while x < 999:
        multiples.append(x * n)
        x += 1

strings = [str(x) for x in multiples]

for i in strings:
    if len(strings[i]) % 2 == 0:
        pass
