# Task 8: Extract Words Starting with a Specific
# Letter (filter and lambda)
# Problem:
# You are given a list of words and a target letter. Use a
# lambda function and filter to create a new list containing
# only the words that start with the given letter.
# Input:
# words = ["apple", "banana", "cherry", "apricot", "blueberry"]
# target_letter = "a"

# Expected Output:
# ["apple", "apricot"]

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"

filtered_words = filter(lambda x: x.startswith(target_letter), words)
filtered_words = list(filtered_words)
print(filtered_words)
