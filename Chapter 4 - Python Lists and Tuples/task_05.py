# Task 5: Swap Values Using Tuples
# Problem:
# Write a program that swaps the values of two variables using tuples.
# 1. Prompt the user to input two values.
# 2. Use a tuple to perform the swap in a single line of code.
# 3. Display the values before and after the swap.
# Example Input:
# Enter first value: 10
# Enter second value: 20

# Expected Output:
# Before Swap: First Value = 10, Second Value = 20
# After Swap: First Value = 20, Second Value = 10

# Two solutions are possible:
# Using python swap method (easy and correct)
# Using arithmetic method (advanced but complicated)
print("\nTASK 5")
first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))
my_tuple = (first_value, second_value)
print(f"Before Swap: First Value = {my_tuple[0]}, Second Value = {my_tuple[1]}")
# Variant 1
print("VARIANT 1")
my_tuple = tuple(reversed(my_tuple))
print(f"After Swap: First Value = {my_tuple[0]}, Second Value = {my_tuple[1]}")
# Variant 2
my_tuple = (first_value, second_value)
a, b = my_tuple
sum = a + b
a = sum - a
b = sum - b
my_tuple = (a, b)
print("VARIANT 2")
print(f"After Swap: First Value = {my_tuple[0]}, Second Value = {my_tuple[1]}")
