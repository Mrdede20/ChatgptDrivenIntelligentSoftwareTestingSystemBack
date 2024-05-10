Here are two programs that achieve the same intention:

Program 1:

```
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        split = text[:cols].rfind(' ')
        if split == -1:
            split = cols
        lines.append(text[:split])
        text = text[split+1:]
    lines.append(text)
    return lines
```

Program 2:

```
def wrap(text, cols):
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        if len(current_line + word) <= cols:
            current_line += word + ' '
        else:
            lines.append(current_line.strip())
            current_line = word + ' '

    lines.append(current_line.strip())
    return lines
```

Both programs achieve the goal of breaking the input text into lines of length `cols` or less. Program 1 loops through the text, finding the last space character before the limit of `cols`. Program 2 splits the text into a list of words and then loops through each word, building up lines until they are too long.

You can use either of these programs to format long paragraphs of text to fit within a defined width.