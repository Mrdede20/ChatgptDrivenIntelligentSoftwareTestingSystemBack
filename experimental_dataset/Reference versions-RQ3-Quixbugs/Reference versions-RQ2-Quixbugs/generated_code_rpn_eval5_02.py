
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b, a = stack.pop(), stack.pop()
            stack.append({
                '+': lambda: a + b,
                '-': lambda: a - b,
                '*': lambda: a * b,
                '/': lambda: a / b,
            }[token]())
        else:
            stack.append(float(token))
    return stack.pop()
