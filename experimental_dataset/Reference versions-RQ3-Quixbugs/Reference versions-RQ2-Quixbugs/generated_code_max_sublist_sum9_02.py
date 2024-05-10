
def find_maximum_sublist_sum(lst):
    max_sum_ending_here = max_sum_so_far = lst[0]
    for num in lst[1:]:
        if max_sum_ending_here < 0:
            max_sum_ending_here = num
        else:
            max_sum_ending_here += num
        if max_sum_ending_here > max_sum_so_far:
            max_sum_so_far = max_sum_ending_here
    return max_sum_so_far
