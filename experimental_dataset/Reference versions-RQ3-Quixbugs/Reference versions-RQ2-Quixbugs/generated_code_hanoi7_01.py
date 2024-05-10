
def hanoi(height, start, target, intermediate):
    if height == 0:
        return []
    else:
        steps = hanoi(height-1, start, intermediate, target)
        steps.append((start, target))
        steps += hanoi(height-1, intermediate, target, start)
        return steps
