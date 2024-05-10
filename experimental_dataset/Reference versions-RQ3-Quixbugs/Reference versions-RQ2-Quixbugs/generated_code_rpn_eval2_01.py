
def rpn_eval(expr):
    def op(operator):
        b, a = stack.pop(), stack.pop()
        if operator == '+':
            stack.append(a + b)
        elif operator == '-':
            stack.append(a - b)
        elif operator == '*':
            stack.append(a * b)
        elif operator == '/':
            stack.append(a / b)
    
    stack = []
    for token in expr:
        if isinstance(token, int):
            stack.append(token)
        elif token in '+-*/':
            op(token)
    return stack[0]
