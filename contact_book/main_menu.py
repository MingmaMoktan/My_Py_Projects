from database_manager import DatabaseManager

def main_menu(db_manager: DatabaseManager) -> None:
    """Handles the main menu interface for the contact book application."""
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            db_manager.create_contact(name, email, phone)
        elif choice == "2":
            print("Contacts List:")
            contacts = db_manager.read_contacts()
            for contact in contacts:
                print(contact)
        elif choice == "3":
            contact_id = input("Enter contact ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            db_manager.update_contact(contact_id, name, email, phone)
        elif choice == "4":
            contact_id = input("Enter contact ID to delete: ")
            db_manager.delete_contact(contact_id)
        elif choice == "5":
            search_term = input("Enter search term: ")
            result = db_manager.search_contact(search_term)
            print("Search Result:")
            print(result)
        elif choice == "6":
            print("Exiting...")
            db_manager.close()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
