
def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = lst[0]
    below = []
    above = []

    for elem in lst[1:]:
        if elem < pivot:
            below.append(elem)
        else:
            above.append(elem)

    if len(below) == k:
        return pivot
    elif len(below) > k:
        return quickselect(below, k)
    else:
        return quickselect(above, k - len(below) - 1)
