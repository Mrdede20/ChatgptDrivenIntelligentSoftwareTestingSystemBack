
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
