
import random

def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]
    else:
        pivot = random.choice(lst)
        lows = [x for x in lst if x < pivot]
        highs = [x for x in lst if x > pivot]
        pivots = [x for x in lst if x == pivot]
        if k < len(lows):
            return quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))
