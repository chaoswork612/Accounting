from datetime import datetime
from decimal import Decimal

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    print(calculate_salary(Decimal(10000), 24))
    print(get_employees())
    print(datetime.now())
