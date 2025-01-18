# Task 3: Loop through a Range with Step
# Problem:
# Use a for loop with range() to print every third number between 10 and 30 (inclusive).
# After printing the numbers, print the sum of these numbers.
# Example Output:

# 10
# 13
# 16
# 19
# 22
# 25
# 28
# Sum: 133

print("\nTASK 3")
start = 10
end = 30
step = 3
current_number = 0
total_sum = 0

for item in range(start, end):
    if current_number == step or current_number == 0:
        print(item)
        total_sum = total_sum + item
    current_number += 1 if current_number < step else -2
print("Sum:", total_sum)
