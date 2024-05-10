
def rpn_eval(tokens):
    # Define the operator functions
    add = lambda a, b: a + b
    subtract = lambda a, b: a - b
    multiply = lambda a, b: a * b
    divide = lambda a, b: a / b if b != 0 else float('nan')
    operators = {'+': add, '-': subtract, '*': multiply, '/': divide}
    
    # Initialize empty stack
    stack = []
    
    # Iterate through tokens
    for token in tokens:
        # Process numbers
        if isinstance(token, float):
            stack.append(token)
        # Process operators
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
    return stack[-1]
