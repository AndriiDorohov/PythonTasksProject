# Task 1: Basic Class and Object Creation
# Problem:
# Create a class Car with the following attributes
# (Use the __init__ method):
# make (string)
# model (string)
# year (integer)
# Create an instance of the class with values for make,
# model, and year.
# Print the instance's attributes.
# Example Output:

# Make: Toyota
# Model: Camry
# Year: 2020


class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\n"


instance = Car("Toyota", "Camry", 2020)
print(instance)
