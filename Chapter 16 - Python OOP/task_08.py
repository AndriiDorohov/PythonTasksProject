# Task 8: Class Method and Static Method
# Problem:
# Create a class Employee with the following:
# name (string)
# salary (float)
# Add a class method from_string() that creates an
# Employee instance from a string in the format "name, salary".
# Add a static method is_high_salary() that checks
# if an employee's salary is above 100,000.
# Demonstrate creating an employee from a string and
# checking their salary.
# Example Output:

# Employee name: Alice, Salary: 120000
# Is the salary high? True


class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, name: str, salary: int):
        return cls(name, salary)

    @staticmethod
    def is_high_salary(salary):
        return (
            "Is the salary high? True"
            if salary > 100000
            else "Is the salary high? False"
        )


employee = Employee.from_string("Alice", 120000)
print(f"Employee name: {employee.name}, Salary: {employee.salary}")
print(employee.is_high_salary(1200000))
