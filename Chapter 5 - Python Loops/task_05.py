# Task 5: Reverse List and Print Indices
# Problem:
# Create a list of strings: ['apple', 'banana', 'cherry', 'date', 'elderberry'].
# Use a loop to:
# Reverse the list without using the reverse() function.
# Print each element along with its index in the reversed list.
# Example Output:

# Index 0: elderberry
# Index 1: date
# Index 2: cherry
# Index 3: banana
# Index 4: apple

# Consider checking on enumerate built-in function

print("\nTASK 5")
fruits_list = ["apple", "banana", "cherry", "date", "elderberry"]
list_length = len(fruits_list)
for index, fruit in enumerate(fruits_list):
    if index < list_length // 2:
        first_element = fruits_list[index]
        last_element = fruits_list[list_length - index - 1]
        fruits_list[index] = last_element
        fruits_list[list_length - index - 1] = first_element
        print(f"Index {index}: {fruits_list[index]}")
    else:
        print(f"Index {index}: {fruits_list[index]}")
# print(fruits_list)
