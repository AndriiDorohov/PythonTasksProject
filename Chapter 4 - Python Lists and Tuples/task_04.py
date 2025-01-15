# Task 4: List Indexing and Slicing
# Problem:
# 1. Create a list of 7 days of the week: ['Monday', 'Tuesday', 'Wednesday',
# 'Thursday', 'Friday', 'Saturday', 'Sunday'].
# 2. Perform the following tasks:
#  - Print the first day of the week.
#  - Print the last day of the week.
#  - Print the middle days (Tuesday to Saturday).
#  - Replace 'Wednesday' with 'Humpday' and print the updated list.
# Example Output:

# First day: Monday
# Last day: Sunday
# Middle days: ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Updated list: ['Monday', 'Tuesday', 'Humpday', 'Thursday', 'Friday', 'Saturday',
# 'Sunday']
print("\nTASK 4")
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
print("First day: ", days_of_week[0])
print("Last day: ", days_of_week[(len(days_of_week) - 1)])
middle_days = []
for i in range(1, len(days_of_week) - 1):
    middle_days.append(days_of_week[i])
print("Middle days: ", middle_days)
day_to_check = "Wednesday"
if day_to_check in days_of_week:
    updated_days = days_of_week
    updated_days[(days_of_week.index("Wednesday"))] = "Humpday"
    print("Updated list: ", updated_days)
