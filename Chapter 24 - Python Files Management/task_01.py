# Task 1: Write User Input to a File
# Problem:
# Create a program that prompts the user to enter their name, age,
# and favorite color. Write this information to a file called
# user_info.txt in the following format:
# Name: [User's Name]
# Age: [User's Age]
# Favorite Color: [User's Favorite Color]

# Example Input:
# Enter your name: Alice
# Enter your age: 25
# Enter your favorite color: Blue

# Expected Output in user_info.txt:
# Name: Alice
# Age: 25
# Favorite Color: Blue


user_info = {
    "Name": input("Enter your name: "),
    "Age": input("Enter your age: "),
    "Favorite Color": input("Enter your favorite color: "),
}

with open("user_info.txt", "w") as file:
    for key, value in user_info.items():
        file.writelines(f"{key}: {value} \n")
        print(f"{key}: {value}")
