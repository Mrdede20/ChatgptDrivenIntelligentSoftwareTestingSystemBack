
def is_valid_parenthesization(parens):
    if not all(ch in '()' for ch in parens):
        return False  # precondition violated
    depth = 0
    for ch in parens:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
