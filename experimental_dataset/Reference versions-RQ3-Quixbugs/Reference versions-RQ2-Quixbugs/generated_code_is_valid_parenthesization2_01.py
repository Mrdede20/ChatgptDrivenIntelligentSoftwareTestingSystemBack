
def is_valid_parenthesization(parentheses):
    depth = 0
    for char in parentheses:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
