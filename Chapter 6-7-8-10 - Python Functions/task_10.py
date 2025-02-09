# Task 10: Chain map and filter
# Problem:
# You are given a list of integers. Use lambda, map,
# and filter together to first double each number,
# then filter out the numbers that are greater than 10.
# Input:
# numbers = [2, 4, 6, 8, 10]

# Expected Output:
# [4, 8, 12]

numbers = [2, 4, 6, 8, 10]

double_and_filter = filter(lambda a: a <= 10, map(lambda x: x * 2, numbers))
print(list(double_and_filter))
