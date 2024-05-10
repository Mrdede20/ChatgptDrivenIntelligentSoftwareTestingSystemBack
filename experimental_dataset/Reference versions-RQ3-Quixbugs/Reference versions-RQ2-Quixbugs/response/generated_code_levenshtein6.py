Sure, here are the two programs which achieve the mentioned intention using a recursive approach.

Program 1:

```python
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

    return 1 + min(insert, delete, replace)
```

Program 2:

```python
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
```

Both programs use the same method name `levenshtein_distance` and the same parameter type, i.e., two input strings `s` and `t`. They both use a recursive approach with the same steps to calculate the minimum Levenshtein distance. The only difference is in the final return statement of program 2, where it checks for the minimum value among the three possible edit operations: insertion, deletion, and replacement. The first program always uses the `min` function to get the minimum of the three values.