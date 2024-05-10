
def is_valid_parenthesization(parentheses):
    depth = 0
    for p in parentheses:
        if p == '(':
            depth += 1
        elif p == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
