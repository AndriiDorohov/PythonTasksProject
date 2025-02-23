# Task 3: Instance Method
# Problem:
# Modify the Rectangle class from Task 2 to include a
# method area() that calculates and returns the area of the
# rectangle (width * height).
# Create an instance and call the area() method to get the
# rectangle's area.
# Example Output:

# Area: 50


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Width: {self.width}\nHeight: {self.height}"

    def area(self) -> int:
        return self.width * self.height


rectangle_instance = Rectangle(5, 10)
print(f"Area: {rectangle_instance.area()}")
