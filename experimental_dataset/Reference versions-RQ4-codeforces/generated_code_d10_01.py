
from bisect import bisect_left

def is_subsequence_non_decreasing(arr):
    n = len(arr)
    last_val = [arr[0]]
    for i in range(1, n):
        pos = bisect_left(last_val, arr[i])
        if pos == len(last_val):
            last_val.append(arr[i])
        else:
            last_val[pos] = arr[i]
    return "YES" if len(last_val) > 0 else "NO"
