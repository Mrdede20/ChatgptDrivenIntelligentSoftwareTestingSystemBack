
def wrap(text, cols):
    if len(text) <= cols:   # if the length of text is less than or equal to cols
        return [text]   # return a list containing only text
    else:
        last_space = text.rfind(' ', 0, cols+1)    # find the last space within the chunk
        if last_space == -1:    # if there is no space within the chunk
            return [text[:cols]] + wrap(text[cols:], cols)   # add the chunk to the list and call the function recursively with remaining text
        else:
            return [text[:last_space]] + wrap(text[last_space+1:], cols)   # add the line before the space to the list and call the function recursively with remaining text
