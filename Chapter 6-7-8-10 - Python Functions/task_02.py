# Task 2: Function with Multiple Return Values
# Problem:
# 1. Write a function min_max_avg(numbers) that takes a list of
# numbers as an argument.
# 2. The function should return three values:
# The minimum value in the list.
# The maximum value in the list.
# The average of the numbers.
# 3. Ensure that the function handles edge cases where the list is
# empty or has only one number.
# Example Output:

# Min: 1, Max: 9, Average: 5.0
#
# Edge Case Example (empty list):
# Min: None, Max: None, Average: None

from random import randint

def min_max_avg(numbers):
    if not numbers:
        # print("Error, list is empty")
        return None, None, None
    elif len(numbers) == 1:
        min, max, avg = numbers[0], numbers[0], numbers[0]
    else:
        min, max, total_sum = numbers[0], numbers[0], numbers[0]
        for i in numbers[1:]:
            if i > max:
                max = i
            if i < min:
                min = i
            total_sum = total_sum + i
        avg = round(total_sum / len(numbers), 2)
    return min, max, avg

numbers = []

for i in range(15):
    numbers.append(randint(0, 50))


print(numbers)
result = min_max_avg(numbers)
print(f'Min: {result[0]}, Max: {result[1]}, Average: {result[2]}')

numbers = []
print(numbers)
result = min_max_avg(numbers)
print(f'Min: {result[0]}, Max: {result[1]}, Average: {result[2]}')
