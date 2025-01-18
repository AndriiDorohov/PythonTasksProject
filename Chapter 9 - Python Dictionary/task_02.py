# Task 2: Dictionary Iteration
# Problem:
# Create a dictionary with at least 5 key-value pairs representing
# student names and their grades:

# grades = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 88,
#     "Diana": 95,
#     "Eve": 78
# }
# Use a for loop to iterate through the dictionary and print each
# student's name and their grade.
# Example Output:

# Alice: 85
# Bob: 92
# Charlie: 88
# Diana: 95
# Eve: 78
print("\nTASK 2")
grades = {"Alice": 85, "Bob": 92, "Charlie": 88, "Diana": 95, "Eve": 78}
for i in grades:
    print(f"{i}: {grades[i]}")
