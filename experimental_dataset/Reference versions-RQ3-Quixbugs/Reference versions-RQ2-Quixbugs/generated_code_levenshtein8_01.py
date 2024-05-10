
def levenshtein_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    elif s[0] == t[0]:
        return levenshtein_distance(s[1:], t[1:])
    else:
        return 1 + min(levenshtein_distance(s[1:], t), levenshtein_distance(s, t[1:]), levenshtein_distance(s[1:], t[1:]))
