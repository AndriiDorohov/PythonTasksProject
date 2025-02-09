# Task 12: Generate Infinite Prime Numbers
# Problem Statement:
# Write a generator function called generate_primes that yields prime numbers indefinitely.
# Use a while loop to check for prime numbers.
# Test the generator by printing the first 10 prime numbers using a for loop and enumerate.
# Example Input:
# primes = generate_primes()
# for i, prime in enumerate(primes):
#     if i >= 10:  # Stop after 10 primes
#         break
#     print(prime)

# Expected Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29


import math


def generate_primes():
    nm = 2
    while True:
        sq = int(math.sqrt(nm))
        for i in range(2, sq + 1):
            if (nm % i) == 0:
                break
        else:
            yield nm
        nm += 1


primes = generate_primes()
for i, prime in enumerate(primes):
    if i >= 10:  # Stop after 10 primes
        break
    print(prime)
