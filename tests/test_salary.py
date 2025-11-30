from decimal import Decimal
from application.salary import calculate_salary


def test_basic_calculation():
    assert calculate_salary(Decimal(100), 20) == Decimal(2000)

def test_zero_days():
    assert calculate_salary(Decimal(150), 0) == Decimal(0)

def test_fractional_amount():
    assert calculate_salary(Decimal(75.50), 10) == Decimal(755.00)

def test_large_numbers():
    assert calculate_salary(Decimal(5000.75), 250) == Decimal(1250187.50)