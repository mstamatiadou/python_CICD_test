import pytest
from my_package.core import greet, add, multiply, divide

def test_greet():
    assert greet("Marina") == "Hello, Marina!"


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (100, 200, 300),
    (-5, 10, 5),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

def test_multiply():
    assert multiply(3, 4) == 12


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

def test_divide():
    assert divide(12, 4) == 3
    assert divide(12.5, 5) == 2.5


def test_divide_by_zero():
    assert divide(5, 0) == "undefined"

def test_divide_zero():
    assert divide(0, 12)  == 0