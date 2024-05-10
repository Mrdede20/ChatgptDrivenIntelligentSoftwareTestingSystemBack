Program 1:

```
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
```

Program 2:

```
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
``` 

Both programs implement the same algorithm recursively, with the base cases being when either string is empty. They only differ in the way they compare the characters and construct the three possible next distances. Program 1 compares the first character of each string, while Program 2 compares the last character of each string (which can be equally efficient). Both programs return the minimum of the three distances plus one, and the result is the Levenshtein distance.