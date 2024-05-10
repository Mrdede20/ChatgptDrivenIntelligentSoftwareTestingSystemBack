Here are two programs that achieve the intention:

Program 1:

```python
def rpn_eval(tokens):
    stack = []
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ops:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(ops[token](x, y))
        else:
            raise TypeError("Invalid type")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]
```

Program 2:

```python
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token == "+":
            y = stack.pop()
            x = stack.pop()
            stack.append(x + y)
        elif token == "-":
            y = stack.pop()
            x = stack.pop()
            stack.append(x - y)
        elif token == "*":
            y = stack.pop()
            x = stack.pop()
            stack.append(x * y)
        elif token == "/":
            y = stack.pop()
            x = stack.pop()
            stack.append(x / y)
        else:
            raise ValueError("Invalid operator")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]
```

Both programs accept a list of tokens in RPN format and evaluate the mathematical expression. The first program uses a dictionary to map operators to lambda functions for performing arithmetic operations, while the second program uses if-else statements to evaluate each operator. Both programs raise ValueError if the expression is not valid and return the evaluated result as a float value.