Sure, here are two programs that achieve the intention you described:

First Program:

```python
def rpn_eval(tokens):
    def op(symbol, a, b):
        if symbol == '+':
            return a + b
        elif symbol == '-':
            return a - b
        elif symbol == '*':
            return a * b
        elif symbol == '/':
            return a / b

    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(token, a, b))

    return stack[0]

# Example usage
tokens = [2.0, 3.0, '+', 4.0, '*']
print(rpn_eval(tokens)) # Output: 20.0
```

Second Program:

```python
def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b
        }[symbol]

    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(token, a, b))

    return stack[0]

# Example usage
tokens = [2.0, 3.0, '+', 4.0, '*']
print(rpn_eval(tokens)) # Output: 20.0
```

Both programs have the same method name and parameter type as specified in the problem description. The only difference between them is the implementation of the `op` function. The first program uses a series of if/else statements to select the correct operation based on the input symbol, while the second program uses a map of symbols to lambda functions to achieve the same result more concisely.