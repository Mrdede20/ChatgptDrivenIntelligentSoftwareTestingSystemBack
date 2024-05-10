
def modified_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != x:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
