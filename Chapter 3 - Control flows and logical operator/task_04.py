# Task 4: Leap Year Checker
# Problem: Write a program that:
# 1. Asks the user to enter a year.
# 2. Checks if the year is a leap year using the following conditions:
#  - A year is a leap year if it is divisible by 4 but not by 100,
#  unless it is also divisible by 400.
# 3. Prints whether the year is a leap year or not.

print("\nTASK 4")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")