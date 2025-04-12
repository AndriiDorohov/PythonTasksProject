# Task 4: Nested Comprehension
# Problem:
# Given a list of lists [[1, 2, 3], [4, 5], [6, 7]], use a
# nested list comprehension to flatten the list into a single list.
# Print the flattened list.
# Example Output:

# [1, 2, 3, 4, 5, 6, 7]


nested_list = [[1, 2, 3], [4, 5], [6, 7]]
# flattened_list = [item[i] for item in nested_list for i in range(len(item))]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)
