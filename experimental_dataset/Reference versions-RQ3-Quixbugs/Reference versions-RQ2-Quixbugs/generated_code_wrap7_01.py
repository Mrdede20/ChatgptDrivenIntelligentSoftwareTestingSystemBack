
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        i = text.rfind(' ', 0, cols + 1)
        if i == -1:
            i = cols
        lines.append(text[:i].rstrip())
        text = text[i:].lstrip()
    lines.append(text)
    return lines
