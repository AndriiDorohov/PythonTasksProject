# Task 9: Create a Running Total (reduce and lambda)
# Problem:
# You are given a list of numbers. Use a lambda function
# and reduce to create a single list that represents a running total.
# Input:
# numbers = [1, 2, 3, 4]

# Expected Output:
# [1, 3, 6, 10]
#
from functools import reduce

numbers = [1, 2, 3, 4]

calculate_running_total = lambda a, b: a + [a[-1] + b]

running_total = reduce(calculate_running_total, numbers, [0])
running_total.remove(0)
print(running_total)
