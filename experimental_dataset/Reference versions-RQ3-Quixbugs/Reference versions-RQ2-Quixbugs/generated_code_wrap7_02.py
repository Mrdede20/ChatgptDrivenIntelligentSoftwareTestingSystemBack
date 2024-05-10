
def wrap(text, cols):
    lines = []
    while text:
        i = cols
        if len(text) <= cols:
            lines.append(text.lstrip())
            break
        while text[i] != ' ':
            i -= 1
        lines.append(text[:i].lstrip())
        text = text[i:].lstrip()
    return lines
