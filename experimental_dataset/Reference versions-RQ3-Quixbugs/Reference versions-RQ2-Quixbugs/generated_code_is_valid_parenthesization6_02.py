
def check_parens(parens):
    stack = []
    for p in parens:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack and set(parens) <= set('()')
