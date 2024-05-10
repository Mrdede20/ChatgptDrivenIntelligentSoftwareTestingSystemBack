
def kth(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    if k <= len(left):
        return kth(left, k)
    else:
        return kth(right, k - len(left))
