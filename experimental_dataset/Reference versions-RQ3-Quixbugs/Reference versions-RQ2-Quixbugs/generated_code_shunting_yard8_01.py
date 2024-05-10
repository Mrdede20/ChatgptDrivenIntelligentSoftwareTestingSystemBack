
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
