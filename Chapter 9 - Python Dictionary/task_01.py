# Task 1: Basic Dictionary Operations
# Problem:
# Create a dictionary representing a person's details:

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York
# }


# Update the "city" field of the dictionary to "San Francisco".
# Add a new key-value pair "job": "Engineer" to the dictionary.
# Print the updated dictionary.
# Example Output:

# {'name': 'Alice', 'age': 25, 'city': 'San Francisco', 'job': 'Engineer'}


print("\nTASK 1")
person = {"name": "Alice", "age": 25, "city": "New York"}
person["city"] = "San Francisco"
person.update({"job": "Engineer"})
print(person)