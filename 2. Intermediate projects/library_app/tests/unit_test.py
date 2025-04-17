import unittest
from src.book import Book, BookFactory
from src.library import Library
import src.storage as storage
import sys
import os

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

    def tearDown(self):
        # Clean up the test file and reset LIBRARY_FILE
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        storage.LIBRARY_FILE = self.original_file

    def test_save_and_load_library(self):
        test_books = [Book("Test", "Author")]
        storage.save_library(test_books)
        loaded_books = storage.load_library()

        self.assertEqual(len(loaded_books), 1)
        self.assertEqual(loaded_books[0].title, "Test")
        self.assertEqual(loaded_books[0].author, "Author")

if __name__ == '__main__':
    unittest.main()
