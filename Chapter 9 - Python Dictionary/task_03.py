# Task 3: Dictionary with Nested Data
# Problem:
# Create a dictionary representing a collection of books, where each
# book has a title, author, and publication year:

# books = {
#     "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
#     "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
# }

# Use a for loop to iterate through the outer dictionary.
# For each book, print the title, author, and year.


# Example Output:

# Book: 1984, Author: George Orwell, Year: 1949
# Book: To Kill a Mockingbird, Author: Harper Lee, Year: 1960

print("\nTASK 3")
books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
}
for i in books:
    print(
        f'Book: {books[i]["title"]}  Author: {books[i]["author"]} Year: {books[i]["year"]}'
    )