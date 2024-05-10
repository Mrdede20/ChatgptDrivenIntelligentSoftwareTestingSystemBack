
def binary_search_lowest_index(lst, target):
    left, right = 0, len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    if lst[left] == target:
        return left
    else:
        return -1
