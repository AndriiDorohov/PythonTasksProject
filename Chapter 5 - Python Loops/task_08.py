# Bonus Task 8: Simulate a Do-While Loop in Python
# Problem:
# Python does not have a built-in do-while loop, but you can simulate one. Write a program that repeatedly asks the user to input a number until they enter a value between 1 and 10. Ensure the first prompt executes at least once, even if the user enters an invalid value.
# Input/Output Example:

# Enter a number between 1 and 10: -5
# Invalid input. Try again.
# Enter a number between 1 and 10: 12
# Invalid input. Try again.
# Enter a number between 1 and 10: 7
# Thank you! Your number is 7.


# Hint for Implementation:
# Use an infinite while True loop to simulate the "do" part.
# Break the loop when the condition is satisfied.
print("\nTASK 8")
while True:
    try:
        number_input = int(input("Enter a number between 1 and 10:  "))
        if number_input >= 1 and number_input <= 10:
            print(f"Thank you! Your number is {number_input}.")
            break
        else:
            print("Invalid input. Try again.")
    except ValueError:
        print("Invalid input. Try again.")
