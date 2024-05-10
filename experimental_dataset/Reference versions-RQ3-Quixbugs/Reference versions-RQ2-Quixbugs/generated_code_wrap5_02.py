
def split_text(text, cols):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= cols:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    return lines
