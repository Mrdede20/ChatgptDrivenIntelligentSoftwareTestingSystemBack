Here's the first implementation using a stack:

```python
def is_valid_parenthesization(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack
```

And here's the second implementation using a counter:

```python
def is_valid_parenthesization(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0
```

Both implementations check if the parentheses are properly nested and return True if they are and False otherwise. The first implementation uses a stack to keep track of opening parentheses, whereas the second implementation uses a counter to keep track of the nesting depth.