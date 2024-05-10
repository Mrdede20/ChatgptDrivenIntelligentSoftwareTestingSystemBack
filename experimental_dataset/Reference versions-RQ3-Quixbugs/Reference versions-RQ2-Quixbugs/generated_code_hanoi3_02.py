
def hanoi(height, start, end, spare):
    if height == 0:
        return []
    else:
        steps = hanoi(height-1, start, spare, end)
        steps += [(start, end)]
        steps += hanoi(height-1, spare, end, start)
        return steps
