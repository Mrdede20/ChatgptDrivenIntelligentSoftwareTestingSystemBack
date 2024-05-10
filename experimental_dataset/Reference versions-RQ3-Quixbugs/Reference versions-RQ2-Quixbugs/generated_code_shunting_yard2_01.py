
def shunting_yard(tokens):
    output = []
    op_stack = []

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while op_stack and precedence[op_stack[-1]] >= precedence[token]:
                output.append(op_stack.pop())
            op_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()

    while op_stack:
        output.append(op_stack.pop())

    return output
