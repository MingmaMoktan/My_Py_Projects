"""
I created this main.py file to manage the library of books.
This is the entry point of the program.
"""
from src.library import Library
import src.storage as storage

def main():
    """
    Main function to run the library management system.
    """
    library = Library()
    library.load(storage.load_library)
    
    while True:
        print("\nLibrary Management System")
        print("1. Show Books")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            library.show_books()
        elif choice == '2':
            library.add_book()
        elif choice == '3':
            library.delete_book()
        elif choice == '4':
            library.save(storage.save_library)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()