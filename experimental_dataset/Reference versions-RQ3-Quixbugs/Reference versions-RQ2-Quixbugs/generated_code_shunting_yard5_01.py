
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
