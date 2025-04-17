"""
I created this library.py file to manage the library of books.
This will load and save the book data to a JSON file.
The library is stored in a JSON file named library.json.
"""
import json
from typing import List
from .book import Book, BookFactory

class Library:
    """
    This class is created to manage the collection of books.
    It provides methods to load, save, show, add, and delete books.
    """
    
    def __init__(self):
        self.book: List[Book] = []
        
    def load(self, loader):
        """
        Load the library from the JSON file.
        Args:
            loader: The function to load the library.
        """
        self.book = loader()
    def save(self, saver):
        """
        Save the library to the JSON file.
        Args:
            saver: The function to save the library.
        """
        saver(self.book)
    def show_books(self):
        """
        Show the list of books in the library.
        """
        if not self.book:
            print("Library empty.")
        else:
            for bk in self.book:
                print(f"Title: {bk.title}, Writer: {bk.author}")
    def add_book(self):
        """
        Add a book to the library.
        """
        t = input("Book title: ")
        a = input("Writer name: ")
        new_book = BookFactory.create_book(t, a)
        self.book.append(new_book)
        print("Book added.")
    def delete_book(self):
        """
        Delete a book from the library.
        """
        t = input("Book title to remove: ")
        self.book = [bk for bk in self.book if bk.title != t]
        print("Book removed.")
        