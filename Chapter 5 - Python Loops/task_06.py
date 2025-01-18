# Task 6: Modify Values in a Nested List
# Problem:
# You are given a nested list that represents a grid of numbers. Your task is to use nested loops to modify some of the values in the grid based on specific conditions.
# Input: A 2D list (nested list) containing integers. Example:

# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Conditions:
# If a number is even, double its value.
# If a number is odd, replace it with 0.
# Output: The modified grid after applying the changes.
# Example output for the given grid:


# [
#     [0, 4, 0],
#     [8, 0, 12],
#     [0, 0, 0]
# ]
print("\nTASK 6")
# Create list
num_rows = 3
num_cols = 3
count = 1
grid = [[count + i + j * num_cols for i in range(num_cols)] for j in range(num_rows)]

for row_index in range(num_rows):
    for col_index in range(num_cols):
        grid[row_index][col_index] = (
            grid[row_index][col_index] * 2 if grid[row_index][col_index] % 2 == 0 else 0
        )
    print(grid[row_index])
