Here are two possible implementations for the `rpn_eval` function in Python:

### Implementation 1

```python
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(token)(a, b))
        else:
            stack.append(float(token))
    return stack.pop()

def op(token):
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }[token]
```

### Implementation 2

```python
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b, a = stack.pop(), stack.pop()
            stack.append({
                '+': lambda: a + b,
                '-': lambda: a - b,
                '*': lambda: a * b,
                '/': lambda: a / b,
            }[token]())
        else:
            stack.append(float(token))
    return stack.pop()
```

Both implementations work in the same way:

Given a list of tokens, the function iterates over them, and if it encounters a number, it stores it in a stack. If it encounters an operator, it pops two numbers from the stack, applies the operator to them using the `op` helper function, and pushes the result back to the stack.

Finally, when it has processed all tokens, it returns the final value left on top of the stack. 

The `op` helper function returns a lambda function corresponding to each mathematical operator, allowing us to easily apply them to the two operands popped from the stack. 

In implementation 2, the `op` function is not needed as the lambdas are defined directly in the code block.