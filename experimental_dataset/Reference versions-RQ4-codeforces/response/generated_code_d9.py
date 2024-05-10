Sure, here are two programs that achieve this intention:

Program 1:

```python
from bisect import bisect_left, bisect_right

def find_valleys(mountains):
    valleys = []
    for i, height in enumerate(mountains):
        if i == 0:
            if height < mountains[i+1]:
                valleys.append(i)
        elif i == len(mountains) - 1:
            if height < mountains[i-1]:
                valleys.append(i)
        else:
            if height < mountains[i-1] and height < mountains[i+1]:
                valleys.append(i)
                
    return valleys

def has_contiguous_sublist(mountains):
    valleys = find_valleys(mountains)
    if len(valleys) < 2:
        return False
    
    for i in range(len(valleys) - 1):
        if valleys[i+1] - valleys[i] > 1:
            return True
        
    return False
```

Program 2:

```python
from bisect import bisect

def find_valleys(mountains):
    valleys = []
    for i, height in enumerate(mountains):
        if i == 0:
            if height < mountains[i+1]:
                valleys.append(i)
        elif i == len(mountains) - 1:
            if height < mountains[i-1]:
                valleys.append(i)
        else:
            if height < mountains[i-1] and height < mountains[i+1]:
                valleys.append(i)
                
    return valleys

def has_contiguous_sublist(mountains):
    valleys = find_valleys(mountains)
    if len(valleys) < 2:
        return False
    
    for i in range(len(valleys) - 1):
        left = bisect(mountains, mountains[valleys[i]], 0, valleys[i]+1)
        right = bisect(mountains, mountains[valleys[i]], valleys[i]+1)
        if valleys[i+1] in range(left, right):
            return True
        
    return False
```

Both programs use the same method name `has_contiguous_sublist` and the same parameter type `mountains`, and they both use the `bisect` or `bisect_left` and `bisect_right` functions from the `bisect` library to perform binary search on the given list of mountains to identify the valleys.

The `find_valleys` function is used by both programs to identify the valleys in the input list of mountains. The `has_contiguous_sublist` function then checks for conditions where a contiguous sublist of valleys exist separating the mountains, and returns `True` if such a sublist exists, and `False` otherwise.