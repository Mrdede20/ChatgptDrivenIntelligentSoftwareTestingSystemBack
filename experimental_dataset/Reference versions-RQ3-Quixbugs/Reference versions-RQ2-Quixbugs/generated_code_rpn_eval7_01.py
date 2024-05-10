
def rpn_eval(tokens):
    def op(symbol, a, b):
        if symbol == '+':
            return a + b
        elif symbol == '-':
            return a - b
        elif symbol == '*':
            return a * b
        elif symbol == '/':
            return a / b
        
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            res = op(token, a, b)
            stack.append(res)
            
    return stack.pop()
