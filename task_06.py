# Task 6: Nested Ternary for Temperature Description
# Problem:
# 1. Create a variable temperature and assign a value to it.
# 2. Use a nested ternary operator to classify the temperature as:
#  - "Cold" if it's less than 15.
#  - "Warm" if it's between 15 and 30 (inclusive).
#  - "Hot" if it's greater than 30.
# 3. Print the classification.
print("\nTASK 6")
temperature = int(input("Enter a temperature: "))
result = "Cold" if (temperature < 15) else "Hot" if (temperature > 30) else "Warm"
print(result)
