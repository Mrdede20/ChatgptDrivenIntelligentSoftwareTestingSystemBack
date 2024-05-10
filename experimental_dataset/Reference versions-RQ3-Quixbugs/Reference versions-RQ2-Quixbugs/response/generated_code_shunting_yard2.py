Here are two implementations for the Shunting-yard algorithm:

Implementation 1:

```python
def shunting_yard(tokens):
    output = []
    op_stack = []

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while op_stack and precedence[op_stack[-1]] >= precedence[token]:
                output.append(op_stack.pop())
            op_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()

    while op_stack:
        output.append(op_stack.pop())

    return output
```

Implementation 2:

```python
def shunting_yard(tokens):
    output = []
    op_stack = []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in "+-*/":
            while op_stack and op_stack[-1] in "+-*/" and ((token in "+-") or (token in "*/" and op_stack[-1] in "*/")):
                output.append(op_stack.pop())
            op_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()

    while op_stack:
        output.append(op_stack.pop())

    return output
```

Both implementations take a list of tokens in infix notation as input, and return the equivalent expression in RPN format. They differ in how they handle operator precedence: implementation 1 uses a dictionary to define operator precedence, while implementation 2 uses conditional statements to compare operator precedence based on their order in the string "+-*/".