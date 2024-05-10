
def quickselect(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
