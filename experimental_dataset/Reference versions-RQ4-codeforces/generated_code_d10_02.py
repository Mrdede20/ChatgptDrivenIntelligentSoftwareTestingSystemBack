
def is_subsequence_non_decreasing(arr):
    n = len(arr)
    last_val = arr[0]
    for i in range(1, n):
        if arr[i] < last_val:
            last_val = arr[i]
        elif arr[i] >= last_val:
            last_val = arr[i]
    return "YES" if last_val is not None else "NO"
