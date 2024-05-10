Here's the first implementation:

```python
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        space_idx = text[:cols + 1].rfind(' ')
        if space_idx == -1:
            space_idx = cols
        lines.append(text[:space_idx])
        text = ' ' + text[space_idx + 1:]
    lines.append(text)
    return lines
```

And here's the second implementation:

```python
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        last_space = text[:cols].rfind(' ')
        if last_space == -1:
            last_space = cols
        lines.append(text[:last_space])
        text = text[last_space:].strip()
    if text:
        lines.append(text)
    return lines
```

Both of these implementations achieve the same goal of breaking up a long string into lines that are no longer than a given column width. They both use a while loop and the `rfind` method to find the last available space character in the text up to the column width limit.

The first implementation stores the remaining text in a new variable called `text`, while the second implementation slices the original `text` variable and strips any leading or trailing whitespace. The second implementation also handles cases where the last line of the text is shorter than the column width.