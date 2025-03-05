from datetime import datetime

class Expense:
    """This class represents the expenses record in personal finance app."""
    def __init__(self, amount: float, timestamp: datetime, category: str, description: str):
        """
        Initializes an Expense object.

        Args:
            amount (float): The amount spent.
            timestamp (datetime): The time of expense.
            category (str): The category of the expense.
            description (str): A brief description.
        """
        self.amount = amount
        self.timestamp = timestamp
        self.category = category
        self.description = description

    def __repr__(self) -> str:
        """Returns a string representation of the Expense object."""
        return f"Expense(amount={self.amount}, timestamp={self.timestamp}, category={self.category}, description={self.description})"
