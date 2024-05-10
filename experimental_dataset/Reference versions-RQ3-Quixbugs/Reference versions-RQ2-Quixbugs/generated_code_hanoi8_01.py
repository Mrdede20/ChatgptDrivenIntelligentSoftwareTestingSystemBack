
def hanoi(n, source=1, auxiliary=2, target=3):
    if n == 1:
        return [(source, target)]
    else:
        move_1 = hanoi(n-1, source, target, auxiliary)
        move_2 = [(source, target)]
        move_3 = hanoi(n-1, auxiliary, source, target)
        return move_1 + move_2 + move_3
