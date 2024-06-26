
def is_valid_parenthesization(parens):
    depth = 0
    
    for char in parens:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                return False
    
    return depth == 0
