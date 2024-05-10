
def to_rpn(tokens):
    # Define operator precedence
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }
    
    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while operators and operators[-1] != "(" and precedence[token] <= precedence[operators[-1]]:
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
    
    while operators:
        output.append(operators.pop())
    
    return output
