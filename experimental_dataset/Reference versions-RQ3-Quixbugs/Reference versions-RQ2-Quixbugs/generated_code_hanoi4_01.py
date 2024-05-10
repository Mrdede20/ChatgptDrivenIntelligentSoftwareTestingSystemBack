
def hanoi(height, start=1, end=3):
    if height == 0:
        return []
    else:
        other = 6 - start - end
        steps = hanoi(height-1, start, other)
        steps.append((start, end))
        steps += hanoi(height-1, other, end)
        return steps
