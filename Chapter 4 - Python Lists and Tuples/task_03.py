# Task 3: List Operations
# Problem:
# 1. Create a list of integers: [5, 12, 7, 9, 20, 15].
# 2 .Perform and print the following operations:
#  - Add a new number 25 to the list.
#  - Remove the number 7 from the list.
#  - Sort the list in ascending order.
#  - Find and print the largest and smallest numbers in the list.
#
# Example Output:
# Original list: [5, 12, 7, 9, 20, 15]
# After adding 25: [5, 12, 7, 9, 20, 15, 25]
# After removing 7: [5, 12, 9, 20, 15, 25]
# Sorted list: [5, 9, 12, 15, 20, 25]
# Largest number: 25
# Smallest number: 5

print("\nTASK 3")
list_int = [5, 12, 7, 9, 20, 15]
print("Original list: ", list_int)
list_int.append(25)
print("After adding 25: ", list_int)
list_int.remove(7)
print("After removing 7: ", list_int)
list_int.sort()
print("Sorted list: ", list_int)
print("Largest number: ", max(list_int))
print("Smallest number: ", min(list_int))
