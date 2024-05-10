
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
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            while opstack and opstack[-1] != '(':
                rpntokens.append(opstack.pop())
            opstack.pop()

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens
