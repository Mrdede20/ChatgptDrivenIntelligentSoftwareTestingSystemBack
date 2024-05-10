
def is_valid_parenthesization(parens):
    stack = []
    for paren in parens:
        if paren == "(":
            stack.append(paren)
        elif paren == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

# Example usage
print(is_valid_parenthesization("(())")) # Output: True
print(is_valid_parenthesization("((())")) # Output: False
