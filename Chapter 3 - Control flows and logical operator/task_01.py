# Task 1: Number Range Checker
# Problem: Write a program that:
# 1. Asks the user to enter a number.
# 2. Checks if the number is:
#  - Less than 10.
#  - Between 10 and 20 (inclusive).
#  - Greater than 20.
# Prints an appropriate message based on the conditions.

number = input("Enter a number:")
number = int(number)
print("\nTASK 1")
if number < 10:
    print("The number is less than 10.")
elif number > 20:
    print("The number is greater than 20. ")
else:
    print("The number is between 10 and 20.")