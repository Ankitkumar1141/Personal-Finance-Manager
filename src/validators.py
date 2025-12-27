from datetime import datetime
from constants import DATE_FORMAT

def validate_amount(amount):
    return amount > 0


def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def format_amount(amount):
    return round(amount, 2)
