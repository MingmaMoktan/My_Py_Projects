"""
I created this storage.py file to manage the storage of book data.
This will load and save the book data to a JSON file.
The library is stored in a JSON file named library.json.
"""

import json
from typing import List
from .book import Book

LIBRARY_FILE = './resources/library.json'

def load_library() -> List[Book]:
    """
    Load the library from the JSON file.
    Returns:
        A list of Book objects.
    """
    try:
        with open(LIBRARY_FILE, 'r') as file:
            data = json.load(file)
            return [Book(**book) for book in data]
    except FileNotFoundError:
        return []

def save_library(library: List[Book]) -> None:
    """
    Save the library to the JSON file.
    Args:
        library: A list of Book objects.
    """
    with open(LIBRARY_FILE, 'w') as file:
        json.dump([book.__dict__ for book in library], file, indent=4)