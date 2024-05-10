
def hanoi(height, start_peg, end_peg, helper_peg):

    if height == 0:
        return []

    # Move the smaller stack to helper peg
    steps = hanoi(height-1, start_peg, helper_peg, end_peg)

    # Move the largest disk to end_peg
    steps.append((start_peg, end_peg))

    # Move the smaller stack from helper peg to end_peg
    steps += hanoi(height-1, helper_peg, end_peg, start_peg)

    return steps
