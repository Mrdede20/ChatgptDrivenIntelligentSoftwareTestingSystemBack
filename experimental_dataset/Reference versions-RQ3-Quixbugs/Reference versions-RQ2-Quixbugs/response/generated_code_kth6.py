Here are two implementations of the QuickSelect algorithm in Python:

**Implementation 1 - Using Recursion:**

```
def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]
    else:
        pivot = lst[0]
        lows = [x for x in lst[1:] if x < pivot]
        highs = [x for x in lst[1:] if x >= pivot]
        num_lows = len(lows)
        if k < num_lows:
            return quickselect(lows, k)
        elif k == num_lows:
            return pivot
        else:
            return quickselect(highs, k - num_lows - 1)
```

**Implementation 2 - Using Iteration:**

```
def quickselect(lst, k):
    pivot = lst[0]
    while True:
        lows = [x for x in lst[1:] if x < pivot]
        highs = [x for x in lst[1:] if x >= pivot]
        num_lows = len(lows)
        if k < num_lows:
            lst = lows
        elif k == num_lows:
            return pivot
        else:
            lst = highs
            k = k - num_lows - 1
            pivot = lst[0]
```

Both implementations achieve the same purpose of finding the kth-lowest element in a list using the QuickSelect algorithm. The first implementation uses recursion while the second implementation uses iteration.