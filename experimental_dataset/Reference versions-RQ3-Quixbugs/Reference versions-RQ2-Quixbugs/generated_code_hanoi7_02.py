
def hanoi(height, start, target, intermediate):
    if height == 0:
        return []
    else:
        smaller_steps = hanoi(height-1, start, intermediate, target)
        larger_step = [(start, target)]
        larger_steps = hanoi(height-1, intermediate, target, start)
        return smaller_steps + larger_step + larger_steps
