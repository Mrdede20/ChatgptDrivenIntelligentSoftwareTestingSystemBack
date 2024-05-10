
def hanoi(height, start, end):
    def hanoi_helper(height, start, end, helper):
        if height == 1:
            return [(start, end)]
        else:
            solution = hanoi_helper(height-1, start, helper, end)
            solution.append((start, end))
            solution += hanoi_helper(height-1, helper, end, start)
            return solution
    
    if height == 0:
        return []
    else:
        return hanoi_helper(height, start, end, 6-start-end)
