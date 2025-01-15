# Task 2: Password Validator
# Problem: Create a program that:
# - Asks the user to enter a password.
# - Checks if the password meets the following criteria:
# - At least 8 characters long.
# - Contains the word "Python".
# - Does not contain any spaces.
# - Prints whether the password is valid or not, and if
# invalid, specifies why.

print("\nTASK 2")
password = input("Enter a password:")
if len(password) < 8:
    print("Passowrd is too short.")
elif " " in password:
    print("The password contains spaces.")
elif "Python" not in password:
    print("Password is invalid.")
else:
    print("Password is valid.")