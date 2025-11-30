from application.db.people import get_employees


def test_get_employees_returns_list():
    assert isinstance(get_employees(), list)


def test_employee_list_length():
    assert len(get_employees()) == 4


def test_all_expected_employees_present():
    expected_employees = ['David', 'Tom', 'Lisa', 'Unknown']
    assert get_employees() == expected_employees


def test_no_unexpected_employees():
    actual_employees = get_employees()
    assert 'Sarah' not in actual_employees
    assert 'Admin' not in actual_employees