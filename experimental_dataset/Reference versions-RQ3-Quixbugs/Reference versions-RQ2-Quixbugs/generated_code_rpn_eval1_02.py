
def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b
        }[symbol]

    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(token, a, b))

    return stack[0]

# Example usage
tokens = [2.0, 3.0, '+', 4.0, '*']
print(rpn_eval(tokens)) # Output: 20.0
