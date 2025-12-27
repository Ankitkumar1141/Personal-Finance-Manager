import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "expenses.csv")

DATE_FORMAT = "%Y-%m-%d"
CSV_HEADERS = ["date", "category", "amount", "description"]
