Here are two versions of the `rpn_eval` function:

Version 1:

```python
def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b
        }[symbol]()
    
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            result = op(token, a, b)
            stack.append(result)
    return stack[-1]
```

Version 2:

```python
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
```

Both versions of the function use the same method name and parameter type. They define an inner function `op` or a dictionary of operator functions, respectively, to perform the appropriate operation given an operator symbol and two operands. They then iterate through the list of tokens, appending numbers to the stack and calling `op` or the appropriate operator function when an operator symbol is encountered. Finally, they return the result left on the stack.