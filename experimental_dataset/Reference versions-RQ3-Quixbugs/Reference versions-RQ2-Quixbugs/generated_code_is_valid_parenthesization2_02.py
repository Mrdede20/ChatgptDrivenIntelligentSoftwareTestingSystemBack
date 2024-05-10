
def is_valid_parenthesization(parentheses):
    stack = []
    for char in parentheses:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
