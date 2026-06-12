# app.py — Basic Calculator
# This file is used across all 4 Claude Code setup demos (Lecture 6.1)

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float | str:
    """Return the result of dividing a by b, or an error message if b is zero."""
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


if __name__ == "__main__":
    print("Basic Calculator")
    print("----------------")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")
    print(f"10 / 0  = {divide(10, 0)}")
