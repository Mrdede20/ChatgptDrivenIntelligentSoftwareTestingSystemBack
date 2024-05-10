
def kth(arr, k):
    if arr:
        pivot = arr[0]
        smaller = [x for x in arr if x < pivot]
        bigger = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]
        if k < len(smaller):
            return kth(smaller, k)
        elif k < len(smaller) + len(pivots):
            return pivots[0]
        else:
            return kth(bigger, k - len(smaller) - len(pivots))
