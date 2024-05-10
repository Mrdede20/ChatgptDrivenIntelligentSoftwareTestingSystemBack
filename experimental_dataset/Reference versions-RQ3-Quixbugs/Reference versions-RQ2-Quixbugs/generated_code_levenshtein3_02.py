
def levenshtein_distance(source, target, memo={}):
    if (source, target) in memo:
        return memo[(source, target)]
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    elif source[0] == target[0]:
        result = levenshtein_distance(source[1:], target[1:], memo)
    else:
        deletion = levenshtein_distance(source[1:], target, memo)
        insertion = levenshtein_distance(source, target[1:], memo)
        substitution = levenshtein_distance(source[1:], target[1:], memo)
        result = 1 + min(deletion, insertion, substitution)
    memo[(source, target)] = result
    return result
