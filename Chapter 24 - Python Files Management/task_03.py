# Task 3: Append and Display File Content
# Problem:
# Create a program that appends a new line to a file called log.txt
# with the current date and time. Then, read and display the entire
# file content.
# If the file doesn't exist, create it.
# Append the current date and time in the format: YYYY-MM-DD HH:MM:SS.
# Print the entire content of the file after the new line is added.
# Example Execution:
# On the first run:
# log.txt created.
# Appended: 2024-12-26 15:00:00

# On the second run:
# Appended: 2024-12-26 15:01:00

# File content:
# 2024-12-26 15:00:00
# 2024-12-26 15:01:00
#
import os
from datetime import datetime

current_date = datetime.today().isoformat(" ", timespec="seconds")
current_directory = os.getcwd()
entries = os.listdir(current_directory)
file_name = "log.txt"

if os.path.exists(file_name):
    with open(file_name, "a") as file:
        file.write(f"\n{current_date}")

else:
    with open(file_name, "w") as file:
        file.write(f"{current_date}")

with open(file_name, "r") as file:
    print("File content:\n" + file.read())
