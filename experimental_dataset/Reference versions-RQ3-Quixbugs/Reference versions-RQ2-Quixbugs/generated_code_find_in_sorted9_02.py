
def binsearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_in_sorted(arr, x):
    return binsearch(arr, 0, len(arr)-1, x)

# Example usage:
arr = [3, 4, 5, 5, 5, 5, 6]
x = 5
print(find_in_sorted(arr, x)) # output: 3
