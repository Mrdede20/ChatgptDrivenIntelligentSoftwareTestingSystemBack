Here are two different implementations of `rpn_eval` function:

First implementation:

```
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    for t in tokens:
        if t in operators:
            y, x = stack.pop(), stack.pop()
            result = operators[t](x, y)
            stack.append(result)
        else:
            stack.append(float(t))
    return stack.pop()
```

Second implementation:

```
def rpn_eval(tokens):
    stack = []
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    def op(op_str, x, y):
        return operators[op_str](x, y)
    for t in tokens:
        if t in operators:
            y, x = stack.pop(), stack.pop()
            result = op(t, x, y)
            stack.append(result)
        else:
            stack.append(float(t))
    return stack.pop()
```

Both implementations use a dictionary of lambda functions to lookup and apply the operator function. The second implementation defines the `op` function inside the `rpn_eval` function, while the first implementation uses the lambda functions directly inside the loop. Both implementations accomplish the same goal and are valid ways of writing the `rpn_eval` function.