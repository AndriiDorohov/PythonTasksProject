# Task 7: Combine Names with Their Lengths (map and lambda)
# Problem:
# You are given a list of names. Use a lambda function and map
# to create a list of tuples, where each tuple contains a name and its length.
# Input:
# names = ["Alice", "Bob", "Charlie"]

# Expected Output:
# [("Alice", 5), ("Bob", 3), ("Charlie", 7)]


names = ["Alice", "Bob", "Charlie"]
res = map(lambda x: (x, len(x)), names)
print(list(res))
