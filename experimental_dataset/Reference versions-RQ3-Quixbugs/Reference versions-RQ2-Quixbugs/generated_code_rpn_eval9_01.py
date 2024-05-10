
def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b
        }[symbol]()
    
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            result = op(token, a, b)
            stack.append(result)
    return stack[-1]
