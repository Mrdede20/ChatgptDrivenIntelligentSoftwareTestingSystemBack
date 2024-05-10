Program 1:

```
def split_text(text, cols):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line + " " + word) <= cols:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines
```

Program 2:

```
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
```

Both programs take in the same parameters: `text` (long string) and `cols` (maximum column width), and return an ordered list of strings where each string is no longer than the specified column width, and the concatenation of the strings returns the original text. The difference between these two programs is the way they handle the current line. In the first program, it is represented as a string, while in the second program it is represented as a list of words.