Here are two programs which solve the Towers of Hanoi problem recursively:

Program 1:

```python
def hanoi(height, start, end):
    if height == 0:
        return []
    else:
        helper = 6 - start - end
        solution = hanoi(height-1, start, helper)
        solution.append((start, end))
        solution += hanoi(height-1, helper, end)
        return solution
```

Program 2:

```python
def hanoi(height, start, end):
    def hanoi_helper(height, start, end, helper):
        if height == 1:
            return [(start, end)]
        else:
            solution = hanoi_helper(height-1, start, helper, end)
            solution.append((start, end))
            solution += hanoi_helper(height-1, helper, end, start)
            return solution
    
    if height == 0:
        return []
    else:
        return hanoi_helper(height, start, end, 6-start-end)
```

Both programs use the same method name and parameter type, and both implement the same recursive strategy for solving the Towers of Hanoi problem. The main difference is in how the recursive function is implemented: program 1 uses a single function with conditional statements to handle the different cases, while program 2 defines an internal helper function to perform the recursion.