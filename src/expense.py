from validators import format_amount

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = format_amount(float(amount))
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        return [self.date, self.category, self.amount, self.description]

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount:.2f} | {self.description}"
