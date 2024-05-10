Program 1: 

```
def shunting_yard(tokens):
    opstack = []
    rpntokens = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    for token in tokens:
        if token.isdigit():
            rpntokens.append(token)
        elif token in precedence:
            while opstack and opstack[-1] in precedence and precedence[opstack[-1]] >= precedence[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
    while opstack:
        rpntokens.append(opstack.pop())
    return rpntokens
```

Program 2: 

```
def shunting_yard(tokens):
    opstack = []
    rpntokens = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    for token in tokens:
        if token.isdigit():
            rpntokens.append(token)
        elif token in precedence:
            while len(opstack) > 0 and opstack[-1] in precedence and precedence[opstack[-1]] >= precedence[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
    while len(opstack) > 0:
        rpntokens.append(opstack.pop())
    return rpntokens
``` 

Both programs implement the same shunting yard algorithm to convert infix notation to Reverse Polish Notation using the same data structures and parameter type. The only difference is in the comparison of the lengths of the `opstack` list in the while loop condition.