
def max_sublist_sum(lst):
    # Initialize variables
    max_sum = 0
    curr_sum = 0

    # Iterate through list
    for num in lst:
        # Calculate current sum
        curr_sum = max(0, curr_sum + num)

        # Update max sum
        max_sum = max(max_sum, curr_sum)

    return max_sum
