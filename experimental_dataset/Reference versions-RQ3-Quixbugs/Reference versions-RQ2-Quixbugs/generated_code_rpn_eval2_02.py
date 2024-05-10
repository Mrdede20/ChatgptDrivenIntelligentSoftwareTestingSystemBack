
def rpn_eval(expr):
    def op(operator):
        b, a = stack.pop(), stack.pop()
        return {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b,
        }[operator]()
    
    stack = []
    for token in expr:
        if isinstance(token, int):
            stack.append(token)
        elif token in '+-*/':
            result = op(token)
            stack.append(result)
    return stack[0]
