
def levenshtein(s, t):
    if not s:
        return len(t)
    if not t:
        return len(s)
    if s[0] == t[0]:
        return levenshtein(s[1:], t[1:])
    return 1 + min(levenshtein(s[1:], t), levenshtein(s, t[1:]), levenshtein(s[1:], t[1:]))

# Example Usage
print(levenshtein("kitten", "sitting")) # Output: 3 (replace "k" with "s", insert "g", replace "e" with "i")
