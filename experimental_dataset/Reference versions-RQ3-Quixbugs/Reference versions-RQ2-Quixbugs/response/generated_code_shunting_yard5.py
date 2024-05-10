Sure, here are two programs that achieve this intention:

Program 1:
```
def shunting_yard(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token in precedence:
            while operator_stack and operator_stack[-1] != '(' and precedence[token] <= precedence[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output
```

Program 2:
```
def shunting_yard(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    for token in tokens:
        if type(token) == int:
            output.append(token)
        elif token in precedence:
            while operator_stack and operator_stack[-1] != '(' and precedence[token] <= precedence[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output
```

Both of these programs take a list of tokens representing an infix notation arithmetic expression as input and implement the shunting yard algorithm to convert that expression into RPN (postfix notation). They use a dictionary of operator precedences to determine the correct order of operations and maintain two stacks, one for operators and one for output, to keep track of intermediate results. The main difference between the programs is in how they check whether a token is an integer versus an operator. The first program uses the `isinstance()` function to check for integers, while the second program uses a type check with the `==` operator. Both implementations should work correctly for the given input.