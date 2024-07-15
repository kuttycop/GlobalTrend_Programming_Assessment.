def arithmetic(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")
    return result
# Example
try:
    num1 = 10
    num2 = 20
    operator = '+'
    result = arithmetic(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")
    operator = '*'
    result = arithmetic(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")
    num1 = 30
    num2 = 10
    operator = '/'
    result = arithmetic(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")
    num1 = 40
    num2 = 30
    operator = '/' 
    result = arithmetic(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")
except ValueError as ve:
    print(ve)