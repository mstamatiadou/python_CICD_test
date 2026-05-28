#function for greeting, with type hints for string input and output
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

#function for adding 2 numbers, with type hints for integers
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

#Function for multiplying 2 numbers, with type hints for integers
def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b

#Function for dividing 2 numbers, with type hints for floats
def divide(a: float, b: float) -> float:
    """Return the product of two integers."""
    return a / b
