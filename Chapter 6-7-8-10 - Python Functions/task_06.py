# Task 6: Find the Larger of Two Numbers
# Problem:
# Write a lambda function to compare two numbers and return the larger one.
# Expected Output Examples:
# larger(10, 20)   # Output: 20
# larger(-5, -10)  # Output: -5
# larger(8, 8)     # Output: 8

larger_number = lambda a, b: max(a,b)

a = int(input("Input a:"))
b = int(input("Input b:"))
print(f'larger({a}, {b}) = {larger_number(a,b)}')
