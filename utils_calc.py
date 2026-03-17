def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponent(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

def absolute(a):
    return abs(a)