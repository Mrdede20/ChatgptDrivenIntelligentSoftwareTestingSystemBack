Here's the first implementation:

```python
def hanoi(height, start, end, helper):
    steps = []
    if height == 1:
        steps.append((start, end))
    else:
        steps += hanoi(height-1, start, helper, end)
        steps.append((start, end))
        steps += hanoi(height-1, helper, end, start)
    return steps
```

And here's the second implementation:

```python
def hanoi(height, start, end, helper):
    steps = []
    if height == 0:
        return steps
    else:
        steps += hanoi(height-1, start, helper, end)
        steps.append((start, end))
        steps += hanoi(height-1, helper, end, start)
    return steps
```

Both implementations achieve the same result, but the second implementation is more efficient as it avoids the unnecessary "if" statement when the height is 1. Instead, it treats the base case as when the height is 0, and returns an empty list of steps.