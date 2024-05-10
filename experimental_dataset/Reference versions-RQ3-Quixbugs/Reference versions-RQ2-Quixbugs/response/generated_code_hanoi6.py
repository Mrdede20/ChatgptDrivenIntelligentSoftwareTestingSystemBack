Here are two possible solutions to the problem:

Solution 1:

```python
def hanoi(height, start=1, end=3):
    if height == 1:
        return [(start, end)]
    else:
        helper = 6 - start - end
        return hanoi(height-1, start, helper) + [(start, end)] + hanoi(height-1, helper, end)
```

Solution 2:

```python
def hanoi(height, start=1, end=3):
    if height == 0:
        return []
    else:
        helper = 6 - start - end
        steps = hanoi(height-1, start, helper)
        steps.append((start, end))
        steps += hanoi(height-1, helper, end)
        return steps
```

Both solutions implement the same algorithm for solving the Towers of Hanoi puzzle. The only difference between them is the way they construct the list of steps to be returned. In solution 1, the list is constructed using concatenation of lists obtained from recursive calls. In solution 2, the list is constructed using appending to a list obtained from recursive calls.