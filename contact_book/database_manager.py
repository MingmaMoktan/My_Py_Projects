from logger import Logger, LogLevel

class DatabaseManager:
    """Handles database operations such as creating, reading, updating, and deleting contacts."""
    
    def __init__(self, db_name: str, logger: Logger):
        self.db_name = db_name
        self.logger = logger
        print(f"Initializing database manager with database: {self.db_name}")

    def connect(self) -> None:
        """Simulates connecting to a database."""
        print("Connecting to the database...")
        success = True
        if not success:
            msg = "Database connection failed"
            self.logger.error(msg)
            raise ConnectionError(msg)

    def create_table(self) -> None:
        """Simulates creating a contacts table."""
        self.logger.info("Table created")
        print("Creating contacts table...")

    def create_contact(self, name: str, email: str, phone: str) -> None:
        """Adds a contact to the database."""
        self.logger.info(f"Contact created:\n - Name: {name}\n - Email: {email}\n - Phone: {phone}")
        print(f"Adding contact: {name}, {email}, {phone}")

    def read_contacts(self) -> list[tuple[str, str, str]]:
        """Returns a list of contacts."""
        print("Listing all contacts...")
        return [("John Doe", "john.doe@example.com", "123-456-7890"), 
                ("Mary Sue", "mary.sue@example.com", "223-456-7890")]

    def search_contact(self, contact_id: str) -> tuple[str, str, str]:
        """Searches for a contact by ID."""
        print(f"Searching for '{contact_id}'")
        return ("Some Name", "email@example.com", "123-123-1234")

    def update_contact(self, contact_id: str, name: str, email: str, phone: str) -> None:
        """Updates an existing contact."""
        self.logger.info(f"Contact updated:\n - ID: {contact_id}\n - Name: {name}\n - Email: {email}\n - Phone: {phone}")
        print(f"Updating contact {contact_id} to: {name}, {email}, {phone}")

    def delete_contact(self, contact_id: str) -> None:
        """Deletes a contact by ID."""
        self.logger.warning(f"Contact deleted:\n - ID: {contact_id}")
        print(f"Deleting contact with ID: {contact_id}")

    def close(self) -> None:
        """Closes the database connection."""
        print("Closing the database connection...")
