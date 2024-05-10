
def levenshtein_distance(s, t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    if s[0] == t[0]:
        return levenshtein_distance(s[1:], t[1:])
    
    insert = levenshtein_distance(s, t[1:])
    delete = levenshtein_distance(s[1:], t)
    replace = levenshtein_distance(s[1:], t[1:])

    if insert <= delete and insert <= replace:
        return 1 + insert
    elif delete <= insert and delete <= replace:
        return 1 + delete
    else:
        return 1 + replace
