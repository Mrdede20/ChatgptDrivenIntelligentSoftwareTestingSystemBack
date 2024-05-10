
def max_sublist_sum(arr):
    """
    Finds the maximum sum of contiguous sublists in a given list of integers using Kadane's algorithm

    Example:
    max_sublist_sum([4, -1, 2, 1]) returns 6

    :param arr: List of integers
    :return: Maximum sum of any contiguous sublist of the list
    """
 
    max_ending_here = max_so_far = arr[0]
 
    for i in arr[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
