
def wrap(text, width):
    lines = []
    start = 0
    while start < len(text):
        end = start + width
        if end > len(text):
            end = len(text)
        lines.append(text[start:end].rstrip())
        if end < len(text) and text[end] != ' ':
            next_space = text.rfind(' ', start, end)
            if next_space != -1:
                end = next_space
                lines[-1] = text[start:end].rstrip()
            else:
                lines[-1] = lines[-1] + '-'
        start = end + 1
    return lines
