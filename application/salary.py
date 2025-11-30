from decimal import Decimal


def calculate_salary(amount_per_day: Decimal, working_days: int) -> Decimal:
    return amount_per_day * working_days