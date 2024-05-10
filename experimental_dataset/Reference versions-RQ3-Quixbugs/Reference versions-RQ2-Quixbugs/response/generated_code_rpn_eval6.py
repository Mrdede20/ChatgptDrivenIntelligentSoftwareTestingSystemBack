Program 1:

```python
def rpn_eval(tokens):
    def op(operator):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }[operator]
    
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            num2, num1 = stack.pop(), stack.pop()
            stack.append(op(token)(num1, num2))
    return stack.pop()
```

Program 2:

```python
def rpn_eval(tokens):
    def op(operator):
        if operator == '+':
            return lambda x, y: x + y
        elif operator == '-':
            return lambda x, y: x - y
        elif operator == '*':
            return lambda x, y: x * y
        elif operator == '/':
            return lambda x, y: x / y
    
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            num2, num1 = stack.pop(), stack.pop()
            stack.append(op(token)(num1, num2))
    return stack.pop()
```
Both programs are valid implementations of the RPN calculator. The first program uses a dictionary to select the lambda function based on the operator symbol, while the second program uses a series of if/elif statements to do the same thing.