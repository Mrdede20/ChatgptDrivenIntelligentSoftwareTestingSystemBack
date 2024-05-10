Here is one way to implement the `pascal` function using nested loops:

```python
def pascal(n):
    if n <= 0:
        return []
    rows = [[1]]
    for i in range(1, n):
        prev_row = rows[-1]
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j] + prev_row[j - 1]
        rows.append(cur_row)
    return rows
```

Here is another way to implement `pascal` using recursion:

```python
def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        rows = pascal(n - 1)
        prev_row = rows[-1]
        cur_row = [1] * n
        for i in range(1, n - 1):
            cur_row[i] = prev_row[i] + prev_row[i - 1]
        rows.append(cur_row)
        return rows
```

Both implementations should work correctly and produce the first `n` rows of Pascal's Triangle as a list of lists. Note that the second implementation uses recursion and may be slower and less efficient than the first implementation.