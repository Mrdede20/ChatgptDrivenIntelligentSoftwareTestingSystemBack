
def shunting_yard(tokens):
    output = []
    op_stack = []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in "+-*/":
            while op_stack and op_stack[-1] in "+-*/" and ((token in "+-") or (token in "*/" and op_stack[-1] in "*/")):
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
