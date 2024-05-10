
def rpn_eval(tokens):
    def op(operator):
        if operator == '+':
            return lambda x, y: x + y
        elif operator == '-':
            return lambda x, y: x - y
        elif operator == '*':
            return lambda x, y: x * y
        elif operator == '/':
            return lambda x, y: x / y
    
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ['+', '-', '*', '/']:
            num2, num1 = stack.pop(), stack.pop()
            stack.append(op(token)(num1, num2))
    return stack.pop()
