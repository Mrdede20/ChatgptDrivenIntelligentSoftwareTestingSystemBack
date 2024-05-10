Here are two programs implementing the same function as described:

Program 1:

```python
def is_valid_parenthesization(parens):
    if not all(ch in '()' for ch in parens):
        return False  # precondition violated
    depth = 0
    for ch in parens:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
```

Program 2:

```python
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
```

Both programs use the same logic to check whether the parentheses are properly nested, by keeping track of the depth or a stack of opening parentheses. The second program uses a stack of opening parentheses to keep track of the nesting levels, while the first program uses a simple depth counter. The choice between these two implementations depends on personal preference and coding style.