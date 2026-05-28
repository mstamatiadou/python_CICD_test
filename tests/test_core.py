import pytest
from my_package.core import greet, add, multiply, divide

# Test cases for the core functions in my_package.core
# Each test function checks the expected output for given inputs, including edge cases.
# The test functions use assertions to validate the results, and some tests are parameterized to cover multiple scenarios efficiently.
# To run these tests, use the command: pytest tests/test_core.py
# Example test cases:
# - test_greet: Checks if the greet function returns the correct greeting message.

def test_greet():
    assert greet("Marina") == "Hello, Marina!"

# - test_add: Validates the addition of two positive integers.
def test_add():
    assert add(2, 3) == 5

# - test_add_negative: Validates the addition of two negative integers.
def test_add_negative():
    assert add(-1, -1) == -2

# - test_add_mixed: Validates the addition of a positive and a negative integer.
@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (100, 200, 300),
    (-5, 10, 5),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# - test_multiply: Validates the multiplication of two positive integers.
def test_multiply():
    assert multiply(3, 4) == 12

# - test_multiply_by_zero: Validates that multiplying any number by zero results in zero.
def test_multiply_by_zero():
    assert multiply(5, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (-2, -3, 6),
    (10, 10, 100),
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected

# - test_divide: Validates the division of two numbers, including a case with floating-point numbers.
def test_divide():
    assert divide(12, 4) == 3
    assert divide(12.5, 5) == 2.5

# - test_divide_by_zero: Validates that dividing by zero raises a ZeroDivisionError.
def test_divide_zero():
    assert divide(0, 12)  == 0
