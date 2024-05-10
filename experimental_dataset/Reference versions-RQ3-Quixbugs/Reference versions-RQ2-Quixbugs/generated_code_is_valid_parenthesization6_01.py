
def check_parens(parens):
    depth = 0
    for p in parens:
        if p == '(':
            depth += 1
        elif p == ')':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0 and set(parens) <= set('()')
