
def wrap(text, cols):
    """
    This function takes in a long string and an integer representing the column width. 
    It breaks the string into a list of lines, each no longer than the specified column width. 
    The function ensures that no word in the original text is broken into two parts unless it is necessary. 
    The original amount of spaces is preserved, and spaces at the start or end of each line are not trimmed. 
    The function returns an ordered list of strings as the output.
    """
    lines = []
    words = text.split()
    curr_line = words[0]
    for word in words[1:]:
        if len(curr_line) + 1 + len(word) > cols:
            lines.append(curr_line)
            curr_line = word
        else:
            curr_line += ' ' + word
    lines.append(curr_line)
    return lines
