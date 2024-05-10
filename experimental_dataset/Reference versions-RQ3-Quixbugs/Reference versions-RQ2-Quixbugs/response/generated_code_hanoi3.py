Here are two programs that implement the Towers of Hanoi puzzle using a recursive algorithm:

Program 1:

```
def hanoi(height, start, end, spare):
    if height == 1:
        return [(start, end)]
    else:
        steps = hanoi(height-1, start, spare, end)
        steps += [(start, end)]
        steps += hanoi(height-1, spare, end, start)
        return steps
```

Program 2:

```
def hanoi(height, start, end, spare):
    if height == 0:
        return []
    else:
        steps = hanoi(height-1, start, spare, end)
        steps += [(start, end)]
        steps += hanoi(height-1, spare, end, start)
        return steps
```

Both programs take in three arguments:
- `height` - the height of the initial stack of disks
- `start` - the numbered peg where the initial stack resides
- `end` - the numbered peg which the stack must be moved onto

The first program returns a list of pairs (a, b) representing the shortest series of steps that solves the puzzle. The second program returns the same list, but includes an additional step that moves the top disk from the starting peg to the spare peg. This extra step is not necessary, but it does not affect the correctness of the algorithm.