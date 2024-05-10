
def hanoi(height, start=1, end=3):
    steps = []
    if height == 0:
        return steps
    other = 6 - start - end
    steps += hanoi(height-1, start, other)
    steps.append((start, end))
    steps += hanoi(height-1, other, end)
    return steps
