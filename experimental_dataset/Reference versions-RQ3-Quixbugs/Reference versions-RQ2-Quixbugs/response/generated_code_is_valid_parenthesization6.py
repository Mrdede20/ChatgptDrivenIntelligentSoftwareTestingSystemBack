Here are two programs that achieve the given intention:

Program 1:

```python
def check_parens(parens):
    depth = 0
    for p in parens:
        if p == '(':
            depth += 1
        elif p == ')':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0 and set(parens) <= set('()')
```

Program 2:

```python
def check_parens(parens):
    stack = []
    for p in parens:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack and set(parens) <= set('()')
```

Both of these programs take a single string input `parens` consisting of only parentheses characters and return `True` if the input string is properly nested and `False` otherwise. The first program uses a depth counter that is incremented and decremented as each opening and closing parenthesis is encountered respectively. The second program uses a stack to keep track of opening parentheses and checks if each closing parenthesis matches with the last opening parenthesis in the stack. Both programs also check if the input string contains only parentheses characters using the set containment check.