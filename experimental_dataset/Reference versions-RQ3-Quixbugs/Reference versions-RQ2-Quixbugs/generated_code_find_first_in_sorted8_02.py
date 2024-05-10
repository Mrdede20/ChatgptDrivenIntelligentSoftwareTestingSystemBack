
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            index = mid
            right = mid - 1
    return index
