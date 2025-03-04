from logger import Logger, LogLevel
from database_manager import DatabaseManager
from main_menu import main_menu

if __name__ == "__main__":
    db_name = "contacts.db"
    logger = Logger("path/to/log_file.log", LogLevel.WARNING)
    db_manager = DatabaseManager(db_name, logger)
    db_manager.connect()
    main_menu(db_manager)
