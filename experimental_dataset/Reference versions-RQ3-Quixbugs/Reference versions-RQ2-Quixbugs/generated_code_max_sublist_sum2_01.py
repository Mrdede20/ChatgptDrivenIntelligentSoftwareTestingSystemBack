
def max_sublist_sum(lst):
    # Initialize variables
    max_sum = lst[0]
    curr_sum = lst[0]

    # Iterate through list
    for num in lst[1:]:
        # Calculate current sum
        curr_sum = max(num, curr_sum + num)

        # Update max sum
        max_sum = max(max_sum, curr_sum)

    return max_sum
