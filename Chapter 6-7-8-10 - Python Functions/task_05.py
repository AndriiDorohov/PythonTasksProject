# Task 5: Calculate the Square of a Number
# Problem:
# Write a lambda function to calculate the square of a given number.
# Expected Output Examples:
# square(4)   # Output: 16
# square(-3)  # Output: 9
# square(0)   # Output: 0

square = lambda x: x*x
n=int(input("Input number: "))
print(f'square({n}) = {square(n)}')
