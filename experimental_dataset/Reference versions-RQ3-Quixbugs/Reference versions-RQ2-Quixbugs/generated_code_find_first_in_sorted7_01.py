
def binary_search_lowest_index(lst, target):
    left, right = 0, len(lst) - 1
    lowest_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            lowest_index = mid
            right = mid - 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return lowest_index
