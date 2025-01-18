# Task 1: Loop through a List and Modify Elements
# Problem:
# Create a list of integers: [3, 7, 1, 9, 4].
# Use a for loop to iterate through the list and:
# Multiply each number by 3.
# Replace numbers greater than 15 with 'Too large'.
# Print the modified list after the loop.
# Example Output:

# [9, 21, 3, 'Too large', 12]

# Consider checking on enumerate built-in function

print("\nTASK 1")

numbers = [3, 7, 1, 9, 4]
print(numbers)

for index, number in enumerate(numbers):
    numbers[index] = "Too large" if (number * 3 > 15) else (number * 3)

print(numbers)
