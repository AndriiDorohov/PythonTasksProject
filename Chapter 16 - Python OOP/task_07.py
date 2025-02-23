# Task 7: Dunder Method (__eq__)
# Problem:
# Create a class Person with attributes name and age.
# Override the __eq__() method to compare two Person
# objects based on their name and age.
# Create two instances of Person and check if they are
# equal using the == operator.
# Example Output:

# Are they equal? True


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age


person1 = Person("Mark", 15)
person2 = Person("Liza", 20)
person3 = Person("Mark", 15)
print("Are they equal?", person1 == person2)
print("Are they equal?", person1 == person3)
