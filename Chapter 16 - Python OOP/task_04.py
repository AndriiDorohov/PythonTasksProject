# Task 4: Inheritance
# Problem:
# Create a class Vehicle with the attributes make, model, and year.
# Create a subclass ElectricCar that inherits from Vehicle and adds
# the attribute battery_size (integer).
# Create an instance of ElectricCar, and print the attributes from
# both Vehicle and ElectricCar.
# Example Output:

# Make: Tesla
# Model: Model S
# Year: 2022
# Battery Size: 100


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.battery_size = battery_size

    def __str__(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nBattery Size: {self.battery_size}"


car = ElectricCar("Tesla", "Model S", 2022, 100)
print(car)
