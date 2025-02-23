# Task 6: Dunder Method (__str__)
# Problem:
# Create a class Book with attributes title,
# author, and year_published.
# Override the __str__() method to return a string in the format:
# "[Title] by [Author] (Published: [Year])"
# Create an instance of Book and print it to see
# the custom string representation.
# Example Output:

# The Great Gatsby by F. Scott Fitzgerald (Published: 1925)


class Book:
    def __init__(self, title: str, author: str, year_published: int) -> None:
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (Published: {self.year_published})"


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book)
