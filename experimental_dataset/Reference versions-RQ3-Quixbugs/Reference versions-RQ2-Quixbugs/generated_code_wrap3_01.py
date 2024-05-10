
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        split = text[:cols].rfind(' ')
        if split == -1:
            split = cols
        lines.append(text[:split])
        text = text[split+1:]
    lines.append(text)
    return lines
