
def rpn_eval(tokens):
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            op_func = ops[token]
            res = op_func(a, b)
            stack.append(res)
            
    return stack.pop()
