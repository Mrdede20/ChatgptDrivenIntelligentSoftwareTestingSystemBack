
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pivot = arr[0]
        lows = [elem for elem in arr if elem < pivot]
        highs = [elem for elem in arr if elem > pivot]
        pivots = [elem for elem in arr if elem == pivot]

        if k < len(lows):
            return quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))
