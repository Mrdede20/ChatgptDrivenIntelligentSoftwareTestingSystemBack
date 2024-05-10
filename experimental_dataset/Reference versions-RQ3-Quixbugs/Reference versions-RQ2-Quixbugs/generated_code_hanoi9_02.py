
def hanoi(height, start_peg, end_peg, helper_peg):

    steps = []
    stack = [(height, start_peg, end_peg, helper_peg)]

    while len(stack) > 0:
        h, start, end, helper = stack.pop()

        if h == 1:
            steps.append((start, end))
        else:
            stack.append((h-1, helper, end, start))
            stack.append((1, start, end, helper))
            stack.append((h-1, start, helper, end))

    return steps
