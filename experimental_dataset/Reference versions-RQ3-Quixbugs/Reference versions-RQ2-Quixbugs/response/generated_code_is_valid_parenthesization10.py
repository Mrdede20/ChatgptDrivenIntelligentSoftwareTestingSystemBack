Here are two variations of the `is_valid_parenthesization` function in Python:

**Program 1**

```
def is_valid_parenthesization(parens):
    depth = 0
    for paren in parens:
        if paren == "(":
            depth += 1
        elif paren == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0

# Example usage
print(is_valid_parenthesization("(())")) # Output: True
print(is_valid_parenthesization("((())")) # Output: False
``` 

**Program 2**

```
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
```

Both of these implementations achieve the same goal of checking whether a given string of parentheses contains a properly nested parentheses or not. The first implementation uses a depth counter to keep track of the opening and closing parentheses. The second implementation uses a stack data structure to keep track of the opening and closing parentheses.