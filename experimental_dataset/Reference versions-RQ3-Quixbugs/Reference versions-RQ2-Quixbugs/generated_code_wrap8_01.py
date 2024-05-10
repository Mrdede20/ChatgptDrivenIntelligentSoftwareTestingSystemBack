
def wrap(text, cols):
    lines = []      # create an empty list to store lines
    while len(text) > cols:
        last_space = text.rfind(' ', 0, cols+1)    # find the last space within the chunk
        if last_space == -1:    # if there is no space within the chunk
            lines.append(text[:cols])   # add the chunk to the list
            text = text[cols:]  # remove the chunk from the text
        else:
            lines.append(text[:last_space])   # add the line before the space to the list
            text = text[last_space+1:]   # remove the line before the space from the text
    lines.append(text)   # add the remaining text to the list
    return lines
