# Task 4: Nested Loops for Matrix Printing
# Problem:
# Create a 2D list (matrix) representing a grid of numbers:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Use a nested for loop to print each row in the matrix on a new line.
# Modify the program to sum the values in each row and print the sum after each row.
# Example Output:

# Row: [1, 2, 3] Sum: 6
# Row: [4, 5, 6] Sum: 15
# Row: [7, 8, 9] Sum: 24

print("\nTASK 4")
# Create list
num_rows = 3
num_cols = 3
count = 1
matrix = [[count + i + j * num_cols for i in range(num_cols)] for j in range(num_rows)]

for i in range(3):
    print(f"Row: {matrix[i]} Sum: {sum(matrix[i])}")
