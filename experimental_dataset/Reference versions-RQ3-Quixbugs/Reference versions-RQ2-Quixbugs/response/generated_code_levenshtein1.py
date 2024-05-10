Here are two programs that achieve this intention:

First program:

```
def levenshtein_distance(source, target):
    if len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)
    elif source[0] == target[0]:
        return levenshtein_distance(source[1:], target[1:])
    else:
        remove_distance = levenshtein_distance(source[1:], target)
        insert_distance = levenshtein_distance(source, target[1:])
        replace_distance = levenshtein_distance(source[1:], target[1:])
        return min(remove_distance, insert_distance, replace_distance) + 1
```

Second program:

```
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
```

Both programs check if either of the input string is empty and return the length of the non-empty string. If both strings are non-empty, it compares the first character of both strings. If the characters are the same, it recursively calls the function by removing the first character from both the strings. If the first characters are not the same, the function recursively calls itself three times by removing the first character from source, removing the first character from target, and by replacing the first character of source with the first character of target. The function returns the minimum of these three options plus one to account for the change made.