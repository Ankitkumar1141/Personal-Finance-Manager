from src.validators import validate_date, validate_amount, validate_category


class Expense:
    def __init__(self, date, category, amount, description=""):
        if not validate_date(date):
            raise ValueError("Invalid date format")

        if not validate_amount(amount):
            raise ValueError("Invalid amount")

        if not validate_category(category):
            raise ValueError("Invalid category")

        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }
