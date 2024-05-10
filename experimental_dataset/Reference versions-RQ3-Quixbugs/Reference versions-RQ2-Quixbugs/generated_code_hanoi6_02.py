
def hanoi(height, start=1, end=3):
    if height == 0:
        return []
    else:
        helper = 6 - start - end
        steps = hanoi(height-1, start, helper)
        steps.append((start, end))
        steps += hanoi(height-1, helper, end)
        return steps
