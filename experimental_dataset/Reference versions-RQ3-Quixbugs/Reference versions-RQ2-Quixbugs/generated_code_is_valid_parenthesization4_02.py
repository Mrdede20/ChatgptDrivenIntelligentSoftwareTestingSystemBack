
def is_valid_parenthesization(parens):
    if not all(ch in '()' for ch in parens):
        return False  # precondition violated
    stack = []
    for ch in parens:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
