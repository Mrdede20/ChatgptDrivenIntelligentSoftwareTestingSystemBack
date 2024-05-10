
def shunting_yard(tokens):
    """Converts infix notation to RPN using Dijkstra's shunting-yard algorithm."""
    rpntokens = []
    opstack = []
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
    for token in tokens:
        if token.isdigit():
            rpntokens.append(token)
        elif token in precedences:
            while opstack and precedences[opstack[-1]] >= precedences[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
    while opstack:
        rpntokens.append(opstack.pop())
    return rpntokens
