Program 1:

```
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
```

Program 2:

```
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
``` 

In both the programs, the name of the function is "wrap", it takes two parameters- 'text' and 'width' of string and integer type respectively, and it returns a list of substrings of 'text' each of maximum length 'width' where each substring is created by breaking the input text on spaces.