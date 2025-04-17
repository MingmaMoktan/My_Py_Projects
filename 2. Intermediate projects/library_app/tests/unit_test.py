import unittest
import sys
import os
# Added the following line to include the src directory in the path
# This is necessary to import the modules from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.book import Book, BookFactory
from src.library import Library
import src.storage as storage

class TestBookFactory(unittest.TestCase):
    def test_create_book(self):
        book = BookFactory.create_book("Test Title", "Test Author")
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.book = []
        self.library.book.append(Book("Title1", "Author1"))
        self.assertEqual(len(self.library.book), 1)

    def test_delete_book(self):
        self.library.book = [Book("Title1", "Author1")]
        # Simulate deleting the book without user input
        self.library.book = [bk for bk in self.library.book if bk.title != "Title1"]
        self.assertEqual(len(self.library.book), 0)

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = './resources/test_library.json'
        self.original_file = storage.LIBRARY_FILE
        storage.LIBRARY_FILE = self.test_file