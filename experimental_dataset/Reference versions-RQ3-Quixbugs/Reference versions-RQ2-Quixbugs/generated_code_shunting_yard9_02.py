
def shunting_yard(tokens):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in operator_precedence:
            while operator_stack and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue
