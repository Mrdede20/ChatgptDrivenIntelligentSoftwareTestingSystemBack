
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a ** b
    }
    
    for token in tokens:
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            op_func = operators[token]
            stack.append(op_func(a, b))
    
    return stack[0]
