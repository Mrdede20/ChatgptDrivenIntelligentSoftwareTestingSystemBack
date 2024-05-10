
def find_first_in_sorted(arr, x):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo if lo < len(arr) and arr[lo] == x else -1
