import pytest
from my_package.core import greet, add

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