
def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1
    resultIndex = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            resultIndex = mid
            hi = mid - 1
        elif x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1 

    return resultIndex
