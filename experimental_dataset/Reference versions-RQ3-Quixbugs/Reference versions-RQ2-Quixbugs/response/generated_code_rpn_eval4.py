Program 1:

```python
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)
    return stack.pop()
```

Program 2:

```python
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    return stack.pop()
```

Both programs achieve the same intention of implementing a RPN calculator to evaluate arithmetic expressions given as tokens in RPN. Both initialize an empty stack, iterate through the list of tokens, and based on the type of token perform the appropriate actions to compute and push the results onto the stack. Each program pops the final result off the stack and returns it as the evaluated result of the RPN expression. Program 1 uses a separate `result` variable to store intermediate calculations while Program 2 uses the `append` method of the stack to push intermediate results.