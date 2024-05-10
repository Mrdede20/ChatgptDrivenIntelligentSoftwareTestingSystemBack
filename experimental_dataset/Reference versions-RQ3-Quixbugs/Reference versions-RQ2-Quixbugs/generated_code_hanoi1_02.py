
def hanoi(height, start=1, end=3):
    moves = []

    def sub_hanoi(height, start, end, spare):
        if height == 0:
            return
        sub_hanoi(height-1, start, spare, end)
        moves.append((start, end))
        sub_hanoi(height-1, spare, end, start)

    sub_hanoi(height, start, end, 6-start-end)
    return moves
