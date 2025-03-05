from typing import List, Optional
from datetime import datetime
from expenses import Expense
from income import Income

class Finance:
    """This is the main class that helps to manage all the incomes and expenses in this personal finance app."""

    def __init__(self):
        """This initializes the Finance manager with empty lists."""
        self.expenses: List[Expense] = []
        self.incomes: List[Income] = []

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Adds an expense to the finance tracker."""
        self.expenses.append(Expense(amount, datetime.now(), category, description))

    def add_income(self, amount: float, source: str, description: str) -> None:
        """Adds an income to the finance tracker."""
        self.incomes.append(Income(amount, datetime.now(), source, description))

    def get_balance(self) -> float:
        """Calculates the current balance (total income - total expenses)."""
        total_income = sum(income.amount for income in self.incomes)
        total_expense = sum(expense.amount for expense in self.expenses)
        return f"Remaining balance = {total_income - total_expense}"

    def search_expense(self, search_term: str) -> Optional[Expense]:
        """Searches for an expense by description."""
        for expense in self.expenses:
            if search_term.lower() in expense.description.lower():
                return f"Your expense is {expense}"
        return None

    def search_income(self, search_term: str) -> Optional[Income]:
        """Searches for an income by description."""
        for income in self.incomes:
            if search_term.lower() in income.description.lower():
                return  f"Your income is {income}"
        return None

    def list_expenses(self) -> List[Expense]:
        """Returns a list of all expenses."""
        return self.expenses

    def list_incomes(self) -> List[Income]:
        """Returns a list of all incomes."""
        return self.incomes
