
calculator.py
- Defines functions used to create a simple calculator.

One function per operation, in order.
"""

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Exponent
def power(a, b):
    return a ** b

# Modulo
def mod(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


