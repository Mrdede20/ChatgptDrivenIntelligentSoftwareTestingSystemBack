Certainly, here are two possible implementations of `rpn_eval` function:

Implementation 1:

```python
def rpn_eval(expr):
    def op(operator):
        b, a = stack.pop(), stack.pop()
        if operator == '+':
            stack.append(a + b)
        elif operator == '-':
            stack.append(a - b)
        elif operator == '*':
            stack.append(a * b)
        elif operator == '/':
            stack.append(a / b)
    
    stack = []
    for token in expr:
        if isinstance(token, int):
            stack.append(token)
        elif token in '+-*/':
            op(token)
    return stack[0]
```

Implementation 2:

```python
def rpn_eval(expr):
    def op(operator):
        b, a = stack.pop(), stack.pop()
        return {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b,
        }[operator]()
    
    stack = []
    for token in expr:
        if isinstance(token, int):
            stack.append(token)
        elif token in '+-*/':
            result = op(token)
            stack.append(result)
    return stack[0]
```

Both implementations use the same method name `rpn_eval` and the same parameter type `expr`, which is a list of values and operators in Reverse Polish Notation. They both create an inner function `op` to perform arithmetic operations based on the operator symbol received as argument. The main difference between these two implementations is the way the `op` function is defined: the first implementation uses a series of `if` statements while the second one uses a dictionary with lambda functions to define the operations.

Both implementations maintain a stack to keep track of the operands and apply the operators to the operands in the stack until there is only one value left. The final output is the result after evaluating all the operators in the list.