# Task 4: Function with Keyword Arguments and Validation
# Problem:
# Write a function create_user(username, email, password, **kwargs) that:
# Takes username, email, and password as required parameters.
# Accepts any additional user details through **kwargs (e.g., age, address).
# Validate that:
# The username is at least 5 characters long.
# The email contains @.
# The password is at least 8 characters long.
# Return a dictionary with the user details if validation is successful,
# or an error message if validation fails.
# Example Output (valid input):

# {'username': 'john123', 'email': 'john@example.com', 'password':
# 'securePass123', 'age': 30}
# Example Output (invalid input):

# "Error: Username must be at least 5 characters, email must contain
# '@', and password must be at least 8 characters long."

def create_user(username, email, password, **kwargs):
    if len(username) < 5:
        return "Error: Username must be at least 5 characters."
    elif "@" not in email:
        return "Error: Email must contain '@'."
    elif len(password) < 8:
        return "Error: Password must be at least 8 characters long."
    user_keys = ["username", "email", "password"]
    user_data = [username, email, password]
    user_info = {info : data for info, data in zip(user_keys, user_data)}
    user_info.update(kwargs)
    return user_info

result = create_user("Andrii", "wedpositive@gmail.com", "andrii123",  age =30)

print(result)
