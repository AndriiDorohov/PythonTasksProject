# Task 11: Generate a Sequence of Squares
# Problem:
# Write a generator function called generate_squares that
# yields the squares of numbers starting from 1 up to a given
# number n (inclusive).
# Use a for loop and the yield keyword to create the generator.
# Test the generator by iterating through it and printing the values.
# Example Input:
# for square in generate_squares(5):
#     print(square)

# Expected Output:
# 1
# 4
# 9
# 16
# 25

# Challenge:
# Use the generator with the sum() function, e.g.,
# sum(generate_squares(4)) should return 30.


def generate_squares(n):
    for i in range(1, n + 1):
        n = i * i
        yield n


for square in generate_squares(5):
    print(square)

print(f"Challenge: {sum(generate_squares(4))}")
