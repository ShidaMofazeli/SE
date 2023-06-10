def divide_numbers(dividend, divisor):
    """Divide two numbers and return the quotient."""
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    quotient = dividend / divisor
    return quotient
