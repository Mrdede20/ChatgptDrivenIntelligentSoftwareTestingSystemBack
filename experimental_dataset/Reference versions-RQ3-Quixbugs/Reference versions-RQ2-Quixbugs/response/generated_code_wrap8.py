Sure, here are the two programs:

Program 1: Using while loop

```
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
```

Program 2: Using recursion

```
def wrap(text, cols):
    if len(text) <= cols:   # if the length of text is less than or equal to cols
        return [text]   # return a list containing only text
    else:
        last_space = text.rfind(' ', 0, cols+1)    # find the last space within the chunk
        if last_space == -1:    # if there is no space within the chunk
            return [text[:cols]] + wrap(text[cols:], cols)   # add the chunk to the list and call the function recursively with remaining text
        else:
            return [text[:last_space]] + wrap(text[last_space+1:], cols)   # add the line before the space to the list and call the function recursively with remaining text
```

Both programs have the same function name `wrap` and the same parameter type `(text, cols)`. They both implement the same logic to wrap the long string `text` into lines of specified width `cols`. Program 1 uses a while loop to break the text into smaller lines, while Program 2 uses recursion to do the same.