
def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]
    else:
        pivot = lst[0]
        lows = [x for x in lst[1:] if x < pivot]
        highs = [x for x in lst[1:] if x >= pivot]
        num_lows = len(lows)
        if k < num_lows:
            return quickselect(lows, k)
        elif k == num_lows:
            return pivot
        else:
            return quickselect(highs, k - num_lows - 1)
