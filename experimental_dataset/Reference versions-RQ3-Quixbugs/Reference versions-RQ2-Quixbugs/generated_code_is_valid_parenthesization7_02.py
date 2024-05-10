
def is_valid_parenthesization(parens):
    stack = []
    
    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    return not stack
