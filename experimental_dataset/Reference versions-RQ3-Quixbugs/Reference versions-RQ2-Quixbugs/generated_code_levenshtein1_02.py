
def levenshtein_distance(source, target):
    if not source:
        return len(target)
    elif not target:
        return len(source)
    elif source[0] == target[0]:
        return levenshtein_distance(source[1:], target[1:])
    else:
        remove_distance = levenshtein_distance(source[1:], target)
        insert_distance = levenshtein_distance(source, target[1:])
        replace_distance = levenshtein_distance(source[1:], target[1:])
        return 1 + min(remove_distance, insert_distance, replace_distance)
