# Task 5: Check if a Number is Even or Odd
# Problem:
# 1. Write a program that asks the user to input a number.
# 2. Use a ternary operator to determine if the number is even or odd.
# 3. Print "Even" if the number is even, otherwise print "Odd".

print("\nTASK 5")
number = int(input("Enter a number: "))
result = "Even" if (number % 2 == 0) else "Odd"
print(result)