import pytest
from quick_calc.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    assert calc.add(5, 3) == 8


def test_subtraction(calc):
    assert calc.subtract(10, 4) == 6


def test_multiplication(calc):
    assert calc.multiply(6, 7) == 42


def test_division(calc):
    assert calc.divide(8, 2) == 4


def test_division_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(5, 0)


def test_add_negative_numbers(calc):
    assert calc.add(-5, -3) == -8


def test_decimal_multiplication(calc):
    assert calc.multiply(2.5, 4) == 10.0


def test_large_number_addition(calc):
    assert calc.add(1_000_000_000, 1_000_000_000) == 2_000_000_000