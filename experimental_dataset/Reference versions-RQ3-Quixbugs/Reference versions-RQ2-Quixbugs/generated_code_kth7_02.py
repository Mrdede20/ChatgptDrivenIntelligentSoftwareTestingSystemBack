
import random

def partition(lst, left, right, pivot_index):
    pivot_value = lst[pivot_index]
    lst[pivot_index], lst[right] = lst[right], lst[pivot_index]
    store_index = left
    for i in range(left, right):
        if lst[i] < pivot_value:
            lst[store_index], lst[i] = lst[i], lst[store_index]
            store_index += 1
    lst[right], lst[store_index] = lst[store_index], lst[right]
    return store_index

def quickselect(lst, left, right, k):
    if left == right:
        return lst[left]
    pivot_index = random.randint(left, right)
    pivot_index = partition(lst, left, right, pivot_index)
    if k == pivot_index:
        return lst[k]
    elif k < pivot_index:
        return quickselect(lst, left, pivot_index - 1, k)
    else:
        return quickselect(lst, pivot_index + 1, right, k)
 
def find_kth_lowest(lst, k):
    return quickselect(lst, 0, len(lst) - 1, k - 1)
