# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.
    
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.
        
    Returns:
        float or str: The result of the arithmetic operation, or a message
                      for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2                                                   
    elif operation == 'divide':
        if num2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        return num1 / num2
    else:
        return "ERROR_UNKNOWN_OPERATION"
