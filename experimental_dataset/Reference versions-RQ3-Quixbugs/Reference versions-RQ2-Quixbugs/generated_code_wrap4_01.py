
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # find last space within cols limit
        last_space = text[:cols].rfind(" ")
        # if no space found, break the word
        if last_space == -1:
            last_space = cols
        # add the line to list and remove it from text
        lines.append(text[:last_space])
        text = text[last_space+1:]
    # add the remaining text to a line
    lines.append(text)
    return lines
