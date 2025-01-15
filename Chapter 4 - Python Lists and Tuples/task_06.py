# Task 6: Unpack Tuples with Mixed Data
# Problem:
# Given a tuple containing mixed data types, write a program to unpack its values into variables and display their types.
# 1. Define a tuple with at least one integer, one float, one string, and one boolean.
# 2. Unpack the tuple into individual variables.
# 3. Print each value and its corresponding type.

# Example Input:
# data = (42, 3.14, "Hello", True)

# Expected Output:
# Integer: 42 (Type: <class 'int'>)
# Float: 3.14 (Type: <class 'float'>)
# String: Hello (Type: <class 'str'>)
# Boolean: True (Type: <class 'bool'>)
print("\nTASK 5")
data = (42, 3.14, "Hello", True)
print(data)
dict_var_names = {}
for i, value in enumerate(data):
    dict_var_names[f"var{i+1}"] = value
    print(f"var{i+1} = {value}")

for var_name, value in dict_var_names.items():
    if isinstance(value, str):
        print(f"String: {value} (Type: {type(value)})")
    elif isinstance(value, bool):
        print(f"Boolean: {value} (Type: {type(value)})")
    elif isinstance(value, int):
        print(f"Integer: {value} (Type: {type(value)})")
    elif isinstance(value, float):
        print(f"Float: {value} (Type: {type(value)})")
    else:
        pass
