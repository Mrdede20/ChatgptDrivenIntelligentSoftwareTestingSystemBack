Here are two different programs that achieve the specified intention:

Program 1:
```python
def wrap_text(original_text, column_width):
    words = original_text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= column_width:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines
```

Program 2:
```python
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
```

Both programs take in the original text and column width as parameters, and return a list of lines. The first program splits the text into individual words and iteratively adds them to a line until the line becomes too long, then starts a new line. The second program finds the last space within the column width and breaks the string at that point, repeating the process until there is less than a full line left.