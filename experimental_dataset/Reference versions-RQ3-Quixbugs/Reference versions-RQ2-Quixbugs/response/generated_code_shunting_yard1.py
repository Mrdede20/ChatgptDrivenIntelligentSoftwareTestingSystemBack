Sure, here are two programs that implement the shunting-yard algorithm in Python with the same method name and parameter type:

Program 1:

```python
def shunting_yard(tokens):
    output = []
    operator_stack = []

    operator_precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in operator_precedence:
            while operator_stack and operator_stack[-1] in operator_precedence and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output
```

Program 2:

```python
def shunting_yard(tokens):
    output = []
    operator_stack = []

    operator_precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in operator_precedence:
            while len(operator_stack) > 0 and operator_stack[-1] in operator_precedence and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while len(operator_stack) > 0:
        output.append(operator_stack.pop())

    return output
```

Both programs take a list of tokens as input and implement the shunting-yard algorithm to convert infix notation to RPN notation. The first program uses the `and` keyword to check if `operator_stack` is not empty and if `operator_stack[-1]` has higher or equal precedence as the current `token`. The second program uses the `>` operator and explicitly checks if `len(operator_stack)` is greater than zero before checking the operator precedence. Both programs use a dictionary to define the operator precedence.