"""
I have created the book.py file to manage the book data.
"""
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({self.title}, {self.author})"
class BookFactory:
    """
    Factory class to create Book instances.
    This will create a Book object with the given title and author.
    Args:
        title: The title of the book.
        author: The author of the book.
        return: A Book object.
    """
    @staticmethod
    def create_book(title: str, author: str) -> Book:
        return Book(title, author)