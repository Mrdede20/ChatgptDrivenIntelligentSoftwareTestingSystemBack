
def check_nested_parentheses(parentheses):
    stack = []
    for p in parentheses:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
