
def break_string_into_lines(text, width):
    lines = []
    while len(text) > width:
        split = text[:width+1].rfind(' ')
        if split == -1:
            split = width
        lines.append(text[:split].strip())
        text = text[split:].strip()
    lines.append(text)
    return lines
