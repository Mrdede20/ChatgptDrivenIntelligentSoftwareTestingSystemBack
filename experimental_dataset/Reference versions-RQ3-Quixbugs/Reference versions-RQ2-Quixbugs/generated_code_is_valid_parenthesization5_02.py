
def is_valid_parenthesization(parentheses):
    depth = 0
    for p in parentheses:
        depth += 1 if p == '(' else -1 if p == ')' else 0
        if depth < 0:
            return False
    return depth == 0
