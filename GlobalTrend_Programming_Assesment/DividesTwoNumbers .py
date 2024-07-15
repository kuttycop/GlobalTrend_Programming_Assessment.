def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result
# Example 
print(divide_numbers(20, 2))   
print(divide_numbers(10, 0))    