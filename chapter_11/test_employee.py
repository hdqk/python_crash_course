# Hector Delgado 5/16/2024

import pytest
from employee import Employee


@pytest.fixture
def employee():
    """An employee instance that will be available to all functions."""
    employee = Employee('hector', 'delgado', 50000)
    return employee


def test_give_default_raise(employee):
    """Test if the default raise of $5000 works."""
    employee.give_raise()
    assert employee.salary == 55000


def test_give_custom_raise(employee):
    """Tests if a custom raise amount works."""
    employee.give_raise(10000)
    assert employee.salary == 60000
