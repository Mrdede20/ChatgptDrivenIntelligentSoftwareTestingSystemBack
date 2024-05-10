
def quickselect(lst, k):
    pivot = lst[0]
    while True:
        lows = [x for x in lst[1:] if x < pivot]
        highs = [x for x in lst[1:] if x >= pivot]
        num_lows = len(lows)
        if k < num_lows:
            lst = lows
        elif k == num_lows:
            return pivot
        else:
            lst = highs
            k = k - num_lows - 1
            pivot = lst[0]
