
def rpn_eval(tokens):
    stack = []
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ops:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(ops[token](x, y))
        else:
            raise TypeError("Invalid type")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]
