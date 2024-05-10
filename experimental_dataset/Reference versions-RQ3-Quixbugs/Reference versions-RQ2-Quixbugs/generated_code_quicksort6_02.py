
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        for element in arr:
            if element < pivot:
                left.append(element)
            else:
                right.append(element)
        return quicksort(left) + [pivot] + quicksort(right)
