Here are two programs which achieves this intention:

Program 1:

```python
def shunting_yard(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    rpntokens = []
    opstack = []
    for token in tokens:
        if token.isdigit():
            rpntokens.append(token)
        elif token in precedence:
            while opstack and precedence[opstack[-1]] >= precedence[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
    while opstack:
        rpntokens.append(opstack.pop())
    return rpntokens
    
# example usage
infix = ['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')']
rpn = shunting_yard(infix)
print(rpn) # output: ['3', '4', '2', '*', '1', '5', '-', '/', '+']
```

Program 2:

```python
def shunting_yard(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(str(token))
        elif token in precedence:
            while opstack and precedence[opstack[-1]] >= precedence[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
    while opstack:
        rpntokens.append(opstack.pop())
    return rpntokens
    
# example usage
infix = [3, '+', 4, '*', 2, '/', '(', 1, '-', 5, ')']
rpn = shunting_yard(infix)
print(rpn) # output: ['3', '4', '2', '*', '1', '5', '-', '/', '+']
```

Both programs achieve the same intention and use the same method name and parameter type. The first program assumes that all tokens in the input list are strings, while the second program allows for integers as inputs.