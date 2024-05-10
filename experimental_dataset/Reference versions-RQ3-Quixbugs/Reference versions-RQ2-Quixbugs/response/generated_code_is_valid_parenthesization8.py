Here are two Python programs that achieve the same intention using the same method name and parameter type:

Program 1:

```
def check_nested_parentheses(parentheses):
    depth = 0
    for p in parentheses:
        if p == '(':
            depth += 1
        elif p == ')':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
```

Program 2:

```
def check_nested_parentheses(parentheses):
    stack = []
    for p in parentheses:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
```

Both of these programs take a string `parentheses` as input and iterate through it to check for proper nesting of the parentheses. The first program uses a simple integer `depth` to keep track of the nesting level, while the second program uses a stack to keep track of the opening parentheses. Both programs return True if the parentheses are properly nested, False otherwise.