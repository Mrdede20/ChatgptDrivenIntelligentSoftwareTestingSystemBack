Program 1:

```python
def hanoi(n, source=1, auxiliary=2, target=3):
    if n == 1:
        return [(source, target)]
    else:
        move_1 = hanoi(n-1, source, target, auxiliary)
        move_2 = [(source, target)]
        move_3 = hanoi(n-1, auxiliary, source, target)
        return move_1 + move_2 + move_3
```

Program 2:

```python
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
```

Both programs use recursion and follow the same algorithm to solve the Towers of Hanoi puzzle. The first program follows a more concise approach by returning the list of moves as a single expression, while the second program uses a helper function to keep track of the moves in a list.