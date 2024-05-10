
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
        if arr[mid] == x:
            index = mid
    return index
