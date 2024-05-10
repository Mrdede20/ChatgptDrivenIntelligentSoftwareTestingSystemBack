
def hanoi(height, start=1, end=3):
    moves = []
    if height == 0:
        return moves
    spare = 6 - start - end
    moves += hanoi(height-1, start, spare)
    moves.append((start, end))
    moves += hanoi(height-1, spare, end)
    return moves
