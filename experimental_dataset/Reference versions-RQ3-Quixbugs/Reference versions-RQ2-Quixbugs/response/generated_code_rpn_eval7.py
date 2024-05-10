Program 1: Using if-else statements

```python
def rpn_eval(tokens):
    def op(symbol, a, b):
        if symbol == '+':
            return a + b
        elif symbol == '-':
            return a - b
        elif symbol == '*':
            return a * b
        elif symbol == '/':
            return a / b
        
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            res = op(token, a, b)
            stack.append(res)
            
    return stack.pop()
```

Program 2: Using a dictionary to map operators to functions

```python
def rpn_eval(tokens):
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            op_func = ops[token]
            res = op_func(a, b)
            stack.append(res)
            
    return stack.pop()
``` 

Both programs will work in the same way i.e. evaluate a mathematical expression in Reverse Polish Notation by using a stack data structure. Both programs define a `op` function as a nested function that takes an operator symbol (+, -, *, /) and two numbers as input and returns the result of the operation. The only difference between them is the implementation of the `op` function. Program 1 uses if-else statements to check the type of operator, while program 2 uses a dictionary to map the operator to the corresponding function.