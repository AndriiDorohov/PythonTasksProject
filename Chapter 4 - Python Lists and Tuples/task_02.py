# Task 2: Random Password Generator
# Problem:
# 1. Create a list of characters containing:
#  - All lowercase letters ('a' to 'z').
#  - All uppercase letters ('A' to 'Z').
#  - Digits ('0' to '9').
# 2. Use random.choices() to generate a random 8-character password.
# 3. Print the generated password.
# Example Output:

# Generated password: X7gK2aLp\

import random

print("\nTASK 2")
list1 = [chr(i) for i in range(97, 123)]
list2 = [chr(i) for i in range(65, 91)]
list3 = [chr(i) for i in range(48, 58)]
alphabet = list1 + list2 + list3
# for i in alphabet:
#     print(i)
password = "".join(random.choices(alphabet, k=8))
print("Generated password:", password)
