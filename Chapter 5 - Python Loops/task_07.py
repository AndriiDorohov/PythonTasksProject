# Task 7: Modify a List Using a While Loop
# Problem:
# You are given a list of integers. Use a while loop to iterate through the list and modify the values based on the following conditions:
# Conditions:
# If a number is negative, set it to 0.
# If a number is positive, double its value.
# If a number is 0, skip it without making any changes.
# Input:

# numbers = [-3, 5, 0, -1, 8, 2]

# Expected Output:
# After applying the conditions, the output should be:

# [0, 10, 0, 0, 16, 4]

print("\nTASK 7")

numbers = [-3, 5, 0, -1, 8, 2]
num = 0
while num < len(numbers):
    numbers[num] = (
        0 if numbers[num] < 0 else (numbers[num] * 2 if numbers[num] > 0 else 0)
    )
    num += 1
print(numbers)