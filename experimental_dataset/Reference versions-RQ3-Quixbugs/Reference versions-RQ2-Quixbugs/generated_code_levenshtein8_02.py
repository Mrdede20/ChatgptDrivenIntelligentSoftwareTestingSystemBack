
def levenshtein_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    elif s[0] == t[0]:
        return levenshtein_distance(s[1:], t[1:])
    else:
        delete_s = levenshtein_distance(s[1:], t)
        delete_t = levenshtein_distance(s, t[1:])
        delete_both = levenshtein_distance(s[1:], t[1:])
        return 1 + min(delete_s, delete_t, delete_both)
