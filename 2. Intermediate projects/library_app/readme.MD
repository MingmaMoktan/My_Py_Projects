# Library Management System
A python-based library management system demonstrating clean architecture, factory design pattern, and JSON persistence.
I build it using the Python Boilerplate template with 'pdoc' documentation and 'pytest' testing.

## Boilerplate Features
- **Documentation**: Auto-generated HTML docs via `pdoc`
- **Testing**: `pytest` with coverage reporting
- **Automation**: `Makefile` for common tasks

## Project Structure
Library/
├── src/
│ ├── init.py # Package initialization
│ ├── book.py # Book class and factory pattern
│ ├── library.py # Core library operations
│ ├── storage.py # JSON persistence layer
│ └── main.py # CLI entry point
├── resources/
│ └── library.json # Book data storage
├── tests/
│ ├── integration/ # (Available for future tests)
│ └── unit/
│ └── unit_test.py # Test cases
├── .coveragerc # Coverage configuration
└── requirements.txt # Dependencies


## Key Features

- **Factory Pattern Implementation**: `BookFactory` for standardized object creation
- **JSON Persistence**: Automatic data storage/retrieval
- **Interactive CLI**: User-friendly menu system
- **Unit Tests**: Comprehensive test coverage for core components

## Quick Start and installtion
python3 -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt


### Running the Application
python -m src.main

### Testing
python -m unittest discover tests/ -v

### Documentation Generation
pdoc src/ -o docs/ --html
open docs/index.html

## Core Components
### Book Management (`book.py`)
class Book:
        """Represents a book with title and author"""
    def init(self, title: str, author: str):
        self.title = title
        self.author = author

class BookFactory:
        """Standardized book creation interface"""
    @staticmethod
    def create_book(title: str, author: str) -> Book:
        return Book(title, author)


### Library Operations (`library.py`)
class Library:
    """Manages book collection with CRUD operations"""
    def add_book(self):
        """Interactive book addition"""
        t = input("Book title: ")
        a = input("Writer name: ")
        self.book.append(BookFactory.create_book(t, a))

    def delete_book(self):
        """Title-based book removal"""
        t = input("Book title to remove: ")
        self.book = [bk for bk in self.book if bk.title != t]
### Data Persistence (`storage.py`)
    def load_library() -> List[Book]:
        """Load books from JSON file"""
    try:
        with open(LIBRARY_FILE, 'r') as file:
        return [Book(**book) for book in json.load(file)]

    def save_library(library: List[Book]) -> None:
        """Save books to JSON file"""
        with open(LIBRARY_FILE, 'w') as file:
        json.dump([book.dict for book in library], file, indent=4)


---

## Testing Overview and Unit Tests (`unit_test.py`)
    class TestBookFactory(unittest.TestCase):
        def test_create_book(self):
            book = BookFactory.create_book("1984", "Orwell")
            self.assertEqual(book.title, "1984")

    class TestLibrary(unittest.TestCase):
        def test_add_book(self):
            lib = Library()
            lib.book.append(Book("Test", "Author"))
            self.assertEqual(len(lib.book), 1)

    class TestStorage(unittest.TestCase):
        def test_load_save(self):
            test_books = [Book("Title", "Author")]
            save_library(test_books)
            loaded = load_library()
            self.assertEqual(loaded.title, "Title")


---

## Usage Example
    Library Management System
    Show Books
    Add Book
    Delete Book
    Save and Exit
    Enter your choice: 2
    Book title: The Great Gatsby
    Writer name: F. Scott Fitzgerald
    Book added.

---

## Documentation Standards

- **Google-style docstrings**: Used for all classes/methods
- **Type hints**: Implemented for function signatures
- **pdoc compatibility**: Automatic HTML documentation generation

---

## Requirements

- Python 3.9+
- Dependencies: None (pure Python implementation)

---

## Future Improvements

1. Add ISBN validation in `BookFactory`
2. Implement exception handling for file operations
3. Develop integration tests for full workflows
4. Create GUI version using Tkinter

---

## License

[MIT License](LICENSE) - Open source for educational use