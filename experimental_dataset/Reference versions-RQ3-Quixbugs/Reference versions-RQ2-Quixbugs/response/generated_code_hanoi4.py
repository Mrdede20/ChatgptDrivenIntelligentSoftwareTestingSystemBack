Here's the first program:
```python
def hanoi(height, start=1, end=3):
    if height == 0:
        return []
    else:
        other = 6 - start - end
        steps = hanoi(height-1, start, other)
        steps.append((start, end))
        steps += hanoi(height-1, other, end)
        return steps
```

Here's the second program:
```python
def hanoi(height, start=1, end=3):
    steps = []
    if height == 0:
        return steps
    other = 6 - start - end
    steps += hanoi(height-1, start, other)
    steps.append((start, end))
    steps += hanoi(height-1, other, end)
    return steps
```

Both programs use the same function name `hanoi()` and take the same parameters `height`, `start`, and `end`. They both follow the same recursive approach to solve the Towers of Hanoi puzzle, and return a list of steps to solve the puzzle. The only difference is the order in which the steps are appended to the list `steps`.