Sure, here are two programs in Python that fulfill the given intention:

Program 1:

```python
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
```

Program 2:

```python
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
```

Both programs use the same method name and input parameter type `is_valid_parenthesization(parentheses)`. The first program uses a depth variable to keep track of the proper nesting of parentheses. The second program uses a stack to keep track of the proper nesting of parentheses.

You can choose either program to check whether the string of parentheses is properly nested or not.