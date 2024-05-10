
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        space_idx = text[:cols + 1].rfind(' ')
        if space_idx == -1:
            space_idx = cols
        lines.append(text[:space_idx])
        text = ' ' + text[space_idx + 1:]
    lines.append(text)
    return lines
