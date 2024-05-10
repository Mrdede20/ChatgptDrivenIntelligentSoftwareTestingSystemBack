
def levenshtein_distance(source, target):
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    elif source[0] == target[0]:
        return levenshtein_distance(source[1:], target[1:])
    else:
        deletion = levenshtein_distance(source[1:], target)
        insertion = levenshtein_distance(source, target[1:])
        substitution = levenshtein_distance(source[1:], target[1:])
        return 1 + min(deletion, insertion, substitution)
