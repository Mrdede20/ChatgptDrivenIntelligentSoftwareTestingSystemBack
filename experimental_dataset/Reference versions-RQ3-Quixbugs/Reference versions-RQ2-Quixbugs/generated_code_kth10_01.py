
def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = lst[0]
    below = [elem for elem in lst[1:] if elem < pivot]
    above = [elem for elem in lst[1:] if elem >= pivot]

    if len(below) == k:
        return pivot
    elif len(below) > k:
        return quickselect(below, k)
    else:
        return quickselect(above, k - len(below) - 1)
