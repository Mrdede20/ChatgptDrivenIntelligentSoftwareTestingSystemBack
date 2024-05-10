
def levenshtein_distance(source, target):
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    if source[-1] == target[-1]:
        cost = 0
    else:
        cost = 1
    return min(levenshtein_distance(source[:-1], target) + 1,
               levenshtein_distance(source, target[:-1]) + 1, 
               levenshtein_distance(source[:-1], target[:-1]) + cost)
