
from bisect import bisect_left

def find_LIS(arr):
    n = len(arr)
    ends = []

    for i in range(n):
        idx = bisect_left(ends, arr[i])
        if idx == len(ends):
            ends.append(arr[i])
        else:
            ends[idx] = arr[i]

    return len(ends)
