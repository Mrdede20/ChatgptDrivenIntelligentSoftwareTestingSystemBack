
def wrap_text(original_text, column_width):
    lines = []
    while len(original_text) > column_width:
        last_space = original_text[:column_width].rfind(" ")
        if last_space == -1:
            lines.append(original_text[:column_width])
            original_text = original_text[column_width:]
        else:
            lines.append(original_text[:last_space])
            original_text = original_text[last_space+1:]
    lines.append(original_text)
    return lines
