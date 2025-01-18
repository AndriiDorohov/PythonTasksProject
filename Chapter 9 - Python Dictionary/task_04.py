# Task 4: Dictionary Search and Deletion
# Problem:
# Create a dictionary representing a phone book:

# phone_book = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210",
#     "Charlie": "555-123-4567"
# }

# Use a conditional statement to check if the contact "Alice"
# exists in the dictionary and print her phone number.
# Delete the contact "Bob" from the dictionary using del.
# Print the updated dictionary after the deletion.
# Example Output (search and delete):

# Alice's phone number: 123-456-7890
# {'Alice': '123-456-7890', 'Charlie': '555-123-4567'}

print("\nTASK 4")
phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-123-4567"}

if "Alice" in phone_book:
    print(f"Alice's phone number: {phone_book['Alice']}")
if "Bob" in phone_book:
    del phone_book["Bob"]
print(phone_book)