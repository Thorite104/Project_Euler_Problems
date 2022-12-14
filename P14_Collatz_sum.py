#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.




def colletz(n):
    chain_length = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            chain_length +=1
        else:
            n = (3*n + 1)
            chain_length += 1
    return chain_length


max_chain_length = 0
best_num = 0

for x in range(1000001):
    if x % 2 != 0:
        if colletz(x) > max_chain_length:
            max_chain_length = colletz(x)
            best_num = x

print(max_chain_length, best_num)
