Sure, here are two python programs to implement the Shunting-Yard algorithm:

Program 1:
```python
def shunting_yard(tokens):
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output
```

Program 2:
```python
def shunting_yard(tokens):
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in {'+', '-', '*', '/'}:
            while stack and stack[-1] in {'+', '-', '*', '/'} and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output
```

Both of the above programs use the same method name `shunting_yard` and the same parameter type `tokens`. They implement the Shunting-Yard algorithm to convert the input tokens in infix notation into equivalent RPN (Postfix Notation). The function returns the same tokens reordered into RPN. The function assumes that the input tokens are either integers or arithmetic operators (+,-,*,/), and uses a stack data structure to achieve the transformation process. The difference between the two programs is only in the way they compare precedences of operators. The first program uses `in precedence` while the second program uses `{'+', '-', '*', '/'}`.