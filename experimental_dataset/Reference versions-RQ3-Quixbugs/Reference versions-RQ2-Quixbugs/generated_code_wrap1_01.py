
def wrap(text, width):
    lines = []
    while len(text) > width:
        space_index = text.rfind(' ',0,width+1)
        if space_index == -1:
            space_index = width
        lines.append(text[:space_index].rstrip())
        text = text[space_index+1:]
    lines.append(text.lstrip())
    return lines
