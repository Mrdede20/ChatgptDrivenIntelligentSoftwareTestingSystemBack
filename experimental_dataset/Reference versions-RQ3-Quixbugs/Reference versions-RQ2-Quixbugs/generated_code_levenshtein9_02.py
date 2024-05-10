
def levenshtein(s, t, memo={}):
    if (s, t) in memo:
        return memo[(s, t)]
    if not s:
        return len(t)
    if not t:
        return len(s)
    if s[0] == t[0]:
        memo[(s, t)] = levenshtein(s[1:], t[1:], memo)
        return memo[(s, t)]
    memo[(s, t)] = 1 + min(levenshtein(s[1:], t, memo), levenshtein(s, t[1:], memo), levenshtein(s[1:], t[1:], memo))
    return memo[(s, t)]

# Example Usage
print(levenshtein("kitten", "sitting")) # Output: 3 (replace "k" with "s", insert "g", replace "e" with "i")
