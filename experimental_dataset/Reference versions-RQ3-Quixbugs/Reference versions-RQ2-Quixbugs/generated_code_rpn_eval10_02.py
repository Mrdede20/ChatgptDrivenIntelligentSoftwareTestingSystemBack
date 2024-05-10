
def rpn_eval(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token == "+":
            y = stack.pop()
            x = stack.pop()
            stack.append(x + y)
        elif token == "-":
            y = stack.pop()
            x = stack.pop()
            stack.append(x - y)
        elif token == "*":
            y = stack.pop()
            x = stack.pop()
            stack.append(x * y)
        elif token == "/":
            y = stack.pop()
            x = stack.pop()
            stack.append(x / y)
        else:
            raise ValueError("Invalid operator")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]
