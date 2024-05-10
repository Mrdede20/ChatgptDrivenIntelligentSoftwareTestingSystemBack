Here is the first version of the `rpn_eval` function:

```python
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a ** b
    }
    
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            op_func = operators[token]
            stack.append(op_func(a, b))
    
    return stack[0]
```

And here is a second version that uses a `try`-`except` block to handle invalid tokens:

```python
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a ** b
    }
    
    for token in tokens:
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            op_func = operators[token]
            stack.append(op_func(a, b))
    
    return stack[0]
```