# Task 1: Random Team Picker
# Problem:
# 1. Create a list of names (e.g., your classmates or colleagues).
# 2. Use random.choice() to randomly select one name to lead a group project.
# 3. Print the selected name.
# Example Output:

# Participants: ['Alice', 'Bob', 'Charlie', 'Diana']
# Selected leader: Charlie

import random

names_list = ["Alice", "Bob", "Charlie", "Diana"]
print("\nTASK 1")
print("Participants: ", names_list)
print("Selected leader: ", random.choice(names_list))