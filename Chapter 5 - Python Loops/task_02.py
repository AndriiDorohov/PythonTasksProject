# Task 2: Sum of Even Numbers in a List
# Problem:
# Create a list of integers: [10, 20, 30, 40, 50, 11, 17, 22].
# Use a for loop to iterate through the list and calculate the sum of only the even numbers.
# Print the sum of even numbers and how many even numbers were found.
# Example Output:

# Sum of even numbers: 172
# Number of even numbers: 6


print("\nTASK 2")
numbers = [10, 20, 30, 40, 50, 11, 17, 22]
print(numbers)
even_sum = 0
count = 0
for item in numbers:
    if item % 2 == 0:
        even_sum += item
        count += 1
print("Sum of even numbers: ", even_sum)
print("Number of even numbers: ", count)
