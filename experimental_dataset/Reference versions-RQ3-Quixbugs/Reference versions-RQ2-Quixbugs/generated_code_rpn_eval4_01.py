
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
