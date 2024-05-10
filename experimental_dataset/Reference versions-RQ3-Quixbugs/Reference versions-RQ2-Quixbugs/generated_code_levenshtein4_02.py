
def levenshtein_distance(source, target, memo={}):
    if (source, target) in memo:
        return memo[(source, target)]
    if len(source) == 0:
        memo[(source, target)] = len(target)
    elif len(target) == 0:
        memo[(source, target)] = len(source)
    elif source[0] == target[0]:
        memo[(source, target)] = levenshtein_distance(source[1:], target[1:], memo)
    else:
        deletion = levenshtein_distance(source[1:], target, memo)
        insertion = levenshtein_distance(source, target[1:], memo)
        substitution = levenshtein_distance(source[1:], target[1:], memo)
        memo[(source, target)] = min(deletion, insertion, substitution) + 1
    return memo[(source, target)]
