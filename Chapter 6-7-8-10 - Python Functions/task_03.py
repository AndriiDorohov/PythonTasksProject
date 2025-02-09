# Task 3: Recursive Function to Calculate Factorial
# Problem:
# Write a recursive function factorial(n) that calculates
# the factorial of a number n (i.e., n!).
# The function should return 1 when n is 0 or 1, and recursively
# multiply the number by the factorial of n-1 for values greater than 1.
# Call the function with different values for n (e.g., 5, 6, 7).
# Example Output:

# 5! = 120
# 6! = 720
# 7! = 5040
from random import randint

def fact_recursive(n):
    if n==1 :
        return 1
    else:
        return n*fact_recursive(n-1)

n = randint(0,20)
print(f'{n}! = {fact_recursive(n)}')
