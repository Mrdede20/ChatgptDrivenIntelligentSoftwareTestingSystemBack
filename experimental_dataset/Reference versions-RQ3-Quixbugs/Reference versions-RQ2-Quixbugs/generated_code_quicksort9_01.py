
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = []
    greater = []
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            lesser.append(arr[i])
        else:
            greater.append(arr[i])
    return quicksort(lesser) + [pivot] + quicksort(greater)
