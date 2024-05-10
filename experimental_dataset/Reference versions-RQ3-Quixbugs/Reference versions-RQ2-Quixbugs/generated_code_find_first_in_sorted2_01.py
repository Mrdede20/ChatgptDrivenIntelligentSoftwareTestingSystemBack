
def find_first_in_sorted(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            # If we reached the first occurrence of x
            if mid == 0 or arr[mid - 1] != x:
                return mid
            # Else, adjust the high parameter to search lower indices
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1
