
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
