Here are two programs that achieve the given intention.

Program 1:

```python
def break_string_into_lines(text, width):
    lines = []
    while len(text) > width:
        split = text[:width+1].rfind(' ')
        if split == -1:
            split = width
        lines.append(text[:split].strip())
        text = text[split:].strip()
    lines.append(text)
    return lines
```

In this program, we iterate over the text and find the last occurrence of a space before reaching the column width. We add that line to our list and continue until there is no more text left. We also strip any extra whitespace from the lines before appending them to our list.

Program 2:

```python
def break_string_into_lines(text, width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    return lines
```

In this program, we split the text into individual words and iterate over the words, adding them to the current line until we reach the column width. Then, we add the current line to our list and start a new line with the current word. We also strip any extra whitespace from the lines before appending them to our list.