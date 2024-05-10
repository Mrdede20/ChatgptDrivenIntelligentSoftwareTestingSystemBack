
def hanoi(height, start, end):
    if height == 0:
        return []
    else:
        helper = 6 - start - end
        solution = hanoi(height-1, start, helper)
        solution.append((start, end))
        solution += hanoi(height-1, helper, end)
        return solution
