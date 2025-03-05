from datetime import datetime

class Income:
    """This class keps the record of the incomes in personal finance app."""

    def __init__(self, amount: float, timestamp: datetime, source: str, description: str):
        """
        Initializes an Income object.

        Args:
            amount (float): The amount earned.
            timestamp (datetime): The time of income.
            source (str): The source of income.
            description (str): A brief description.
        """
        self.amount = amount
        self.timestamp = timestamp
        self.source = source
        self.description = description

    def __repr__(self) -> str:
        """Returns a string representation of the Income object."""
        return f"Income(amount={self.amount}, timestamp={self.timestamp}, source={self.source}, description={self.description})"
