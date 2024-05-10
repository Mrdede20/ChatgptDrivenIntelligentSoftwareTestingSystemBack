
def next_permutation(perm: List[int]) -> Optional[List[int]]:
    # Find the pivot position - the index of the last element in a non-increasing suffix
    pivot = len(perm) - 2
    while pivot >= 0 and perm[pivot] >= perm[pivot + 1]:
        pivot -= 1
    
    # If no pivot is found, the sequence is already the last permutation
    if pivot < 0:
        return None
    
    # Find the rightmost element greater than the pivot and swap them
    successor = len(perm) - 1
    while perm[successor] <= perm[pivot]:
        successor -= 1
    perm[pivot], perm[successor] = perm[successor], perm[pivot]
    
    # Reverse the suffix
    perm[pivot + 1:] = perm[-1:pivot:-1]
    
    return perm
