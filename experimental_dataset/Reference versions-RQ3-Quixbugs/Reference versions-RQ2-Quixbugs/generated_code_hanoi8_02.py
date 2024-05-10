
def hanoi(n, source=1, auxiliary=2, target=3):
    moves = []
    if n == 0:
        return moves
    def helper(n, source, auxiliary, target):
        if n == 1:
            moves.append((source, target))
        else:
            helper(n-1, source, target, auxiliary)
            moves.append((source, target))
            helper(n-1, auxiliary, source, target)
    helper(n, source, auxiliary, target)
    return moves
