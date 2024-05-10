
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_greater = []
        items_lower = []
        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return quickSort(items_lower) + [pivot] + quickSort(items_greater)
