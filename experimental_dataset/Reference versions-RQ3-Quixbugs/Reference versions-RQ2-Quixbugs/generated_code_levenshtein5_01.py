
def levenshtein_distance(source, target):
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    elif source[0] == target[0]:
        return levenshtein_distance(source[1:], target[1:])
    else:
        delete_distance = levenshtein_distance(source[1:], target) + 1
        insert_distance = levenshtein_distance(source, target[1:]) + 1
        replace_distance = levenshtein_distance(source[1:], target[1:]) + 1
        return min(delete_distance, insert_distance, replace_distance)
