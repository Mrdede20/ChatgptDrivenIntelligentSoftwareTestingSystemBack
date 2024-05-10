
def hanoi(height, start, end, middle):
    if height == 0:
        return []
    else:
        moves = hanoi(height - 1, start, middle, end)
        moves.append((start, end))
        moves += hanoi(height - 1, middle, end, start)
        return moves
