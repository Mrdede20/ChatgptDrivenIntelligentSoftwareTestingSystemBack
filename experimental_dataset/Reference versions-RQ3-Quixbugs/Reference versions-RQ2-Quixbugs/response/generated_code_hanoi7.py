Sure, here are two programs that implement the Towers of Hanoi puzzle using recursion:

Program 1:

```
def hanoi(height, start, target, intermediate):
    if height == 0:
        return []
    else:
        steps = hanoi(height-1, start, intermediate, target)
        steps.append((start, target))
        steps += hanoi(height-1, intermediate, target, start)
        return steps
```

Program 2:

```
def hanoi(height, start, target, intermediate):
    if height == 0:
        return []
    else:
        smaller_steps = hanoi(height-1, start, intermediate, target)
        larger_step = [(start, target)]
        larger_steps = hanoi(height-1, intermediate, target, start)
        return smaller_steps + larger_step + larger_steps
```

Both programs use the same function name and parameter types. The first program uses the `+=` operator to concatenate the lists returned by the recursive calls, while the second program uses the `+` operator. Both programs achieve the same result and are efficient for solving the Towers of Hanoi puzzle.