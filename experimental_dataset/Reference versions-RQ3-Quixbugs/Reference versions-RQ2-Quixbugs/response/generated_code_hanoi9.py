Sure, here are two possible implementations of the `hanoi` function in Python:

First implementation using recursion:

```python
def hanoi(height, start_peg, end_peg, helper_peg):

    if height == 0:
        return []

    # Move the smaller stack to helper peg
    steps = hanoi(height-1, start_peg, helper_peg, end_peg)

    # Move the largest disk to end_peg
    steps.append((start_peg, end_peg))

    # Move the smaller stack from helper peg to end_peg
    steps += hanoi(height-1, helper_peg, end_peg, start_peg)

    return steps
```

Second implementation using an iterative approach:

```python
def hanoi(height, start_peg, end_peg, helper_peg):

    steps = []
    stack = [(height, start_peg, end_peg, helper_peg)]

    while len(stack) > 0:
        h, start, end, helper = stack.pop()

        if h == 1:
            steps.append((start, end))
        else:
            stack.append((h-1, helper, end, start))
            stack.append((1, start, end, helper))
            stack.append((h-1, start, helper, end))

    return steps
```

Both implementations take in the same parameters - the `height` of the initial stack of disks, as well as the `start_peg` and `end_peg` where the stack starts and must be moved onto, and the `helper_peg` that is not the start or end peg. They both return an ordered list of pairs representing the steps taken to move the stack of disks to the required peg.