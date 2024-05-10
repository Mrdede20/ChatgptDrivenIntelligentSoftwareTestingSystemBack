
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(token)(a, b))
        else:
            stack.append(float(token))
    return stack.pop()

def op(token):
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }[token]
