
def hanoi(height, start, end, helper):
    steps = []
    if height == 1:
        steps.append((start, end))
    else:
        steps += hanoi(height-1, start, helper, end)
        steps.append((start, end))
        steps += hanoi(height-1, helper, end, start)
    return steps
