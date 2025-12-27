from datetime import datetime
from src.constants import DATE_FORMAT


def validate_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0


def validate_category(category: str) -> bool:
    return isinstance(category, str) and len(category.strip()) > 0
