
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = []
    greater = []

    for i in arr[1:]:
        if i < pivot:
            lesser.append(i)
        else:
            greater.append(i)

    return quicksort(lesser) + [pivot] + quicksort(greater)
