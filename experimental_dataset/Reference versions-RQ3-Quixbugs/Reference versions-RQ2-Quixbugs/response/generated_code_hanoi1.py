Program 1:

```python
def hanoi(height, start=1, end=3):
    moves = []
    if height == 0:
        return moves
    spare = 6 - start - end
    moves += hanoi(height-1, start, spare)
    moves.append((start, end))
    moves += hanoi(height-1, spare, end)
    return moves
```

Program 2:

```python
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
```

Both programs implement the algorithm to solve the Tower of Hanoi problem using recursion. The first program has a single function that takes three parameters, whereas the second program has an outer function with the same signature that calls an inner function to perform the recursive steps.