
def find_first_in_sorted(arr, x):
    lo, hi = 0, len(arr) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == x:
            result = mid
            hi = mid - 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1

    return result
