Here are two solutions using the same method name and parameter type:

Solution 1:

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

Solution 2:

```
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
```

Both solutions follow the same logic of iterating over each character in the string and keeping track of the depth/stack of the parentheses. Solution 1 uses the depth variable to keep track of the number of opening brackets encountered and checks for errors by ensuring that the depth never becomes negative. Solution 2 uses a stack data structure to keep track of the opening brackets encountered and checks for errors by ensuring that there is always an opening bracket to match with the closing bracket encountered.