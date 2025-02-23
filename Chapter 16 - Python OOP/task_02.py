# Task 2: Constructor Method (__init__)
# Problem:
# Create a class Rectangle with the following attributes:
# width (integer)
# height (integer)
# Use the __init__ method to initialize the attributes
# when an object is created.
# Create an instance of Rectangle and print its width and height.
# Example Output:

# Width: 5
# Height: 10


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Width: {self.width}\nHeight: {self.height}"


rectangle_instance = Rectangle(5, 10)
print(rectangle_instance)
