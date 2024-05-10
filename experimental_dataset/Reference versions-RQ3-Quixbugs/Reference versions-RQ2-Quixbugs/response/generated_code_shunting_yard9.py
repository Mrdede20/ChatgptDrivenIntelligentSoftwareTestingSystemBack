Program 1:

```python
def shunting_yard(tokens):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in operator_precedence:
            while operator_stack and operator_stack[-1] in operator_precedence \
                    and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue
```

Program 2:

```python
def shunting_yard(tokens):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in operator_precedence:
            while operator_stack and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue
```

Both programs implement the Shunting-Yard algorithm to convert an infix expression to Reverse Polish Notation (RPN). They take a list of tokens in infix notation as input and return the equivalent RPN notation. The only difference between the two programs is that the first one includes an extra check to ensure that the current operator has higher precedence than the top of the operator stack, whereas the second one only checks for lower or equal precedence.