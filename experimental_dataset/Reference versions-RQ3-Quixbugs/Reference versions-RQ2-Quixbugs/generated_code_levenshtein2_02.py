
def levenshtein_distance(source, target):
    if not source:
        return len(target)
    if not target:
        return len(source)

    if source[0] == target[0]:
        return levenshtein_distance(source[1:], target[1:])

    insert = levenshtein_distance(source, target[1:])
    delete = levenshtein_distance(source[1:], target)
    substitute = levenshtein_distance(source[1:], target[1:])

    return 1 + min(insert, delete, substitute)
