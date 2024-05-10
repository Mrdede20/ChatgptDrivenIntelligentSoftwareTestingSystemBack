
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        last_space = text[:cols].rfind(' ')
        if last_space == -1:
            last_space = cols
        lines.append(text[:last_space])
        text = text[last_space:].strip()
    if text:
        lines.append(text)
    return lines
