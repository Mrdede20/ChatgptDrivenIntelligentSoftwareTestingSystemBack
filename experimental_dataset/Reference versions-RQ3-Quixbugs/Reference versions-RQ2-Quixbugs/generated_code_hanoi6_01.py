
def hanoi(height, start=1, end=3):
    if height == 1:
        return [(start, end)]
    else:
        helper = 6 - start - end
        return hanoi(height-1, start, helper) + [(start, end)] + hanoi(height-1, helper, end)
