
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    def op(op_str, x, y):
        return operators[op_str](x, y)
    for t in tokens:
        if t in operators:
            y, x = stack.pop(), stack.pop()
            result = op(t, x, y)
            stack.append(result)
        else:
            stack.append(float(t))
    return stack.pop()
