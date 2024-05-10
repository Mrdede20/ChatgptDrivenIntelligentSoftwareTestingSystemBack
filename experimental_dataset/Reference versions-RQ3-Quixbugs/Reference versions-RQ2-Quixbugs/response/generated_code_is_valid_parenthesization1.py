Program 1:

```
def is_valid_parenthesization(parens):
    stack = []
    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
```

Program 2:

```
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
```

Both programs achieve the same functionality, taking in a string of parenthesis and returning `True` if they are properly nested and `False` otherwise. The first program uses a stack to keep track of opening parentheses and removes them as they are matched with the closing parentheses. If there are any leftover opening parentheses at the end, it returns `False`.

The second program uses a depth counter to keep track of the number of opening parentheses - closing parentheses pairs encountered. If at any point, the counter goes below 0, it means there is a closing parenthesis before its corresponding opening parenthesis and returns `False`. At the end of the loop, if the depth counter is 0, it means all opening parentheses have their corresponding closing parentheses and returns `True`.