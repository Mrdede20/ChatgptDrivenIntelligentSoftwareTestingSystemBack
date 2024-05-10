
from itertools import chain, combinations

def get_all_subsets(lst):
    """
    Takes a list and returns a list of all possible subsets, including the empty set.

    Args:
    lst: list - The original list of items
    
    Returns:
    res: list - A list of lists containing all possible subsets of the input list
    
    Example Usage:
    >>> get_all_subsets([1,2,3])
    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    """
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))
