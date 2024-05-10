
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        items_greater = [item for item in arr[1:] if item > pivot]
        items_lower = [item for item in arr[1:] if item <= pivot]
        return quickSort(items_lower) + [pivot] + quickSort(items_greater)
