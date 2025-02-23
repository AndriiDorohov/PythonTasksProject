# Task 5: Method Overriding
# Problem:
# In Task 4, override the __init__ method of ElectricCar
# to initialize both the attributes of Vehicle and ElectricCar
# (using super()).
# Call the __init__ method from ElectricCar and print the
# values of all attributes.
# Example Output:

# Make: Tesla
# Model: Model X
# Year: 2023
# Battery Size: 120


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year


class ElectricCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, battery_size: int):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def __str__(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nBattery Size: {self.battery_size}"


electric_car = ElectricCar("Tesla", "Model X", 2023, 120)
print(electric_car)
