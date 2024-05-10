Program 1:

```python
def pascal(n):
    rows = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(rows[i-1][j-1] + rows[i-1][j])
        row.append(1)
        rows.append(row)
    return rows
```

Program 2:

```python
def pascal(n):
    if n == 1:
        return [[1]]
    else:
        rows = pascal(n-1)
        row = [1]
        for i in range(1, n-1):
            row.append(rows[-1][i-1] + rows[-1][i])
        row.append(1)
        rows.append(row)
        return rows
```

Both programs achieve the same intention of generating the first n rows of Pascal's triangle and returning them as a list of n lists. Program 1 uses a straightforward iterative approach to generate each row, while Program 2 uses a recursive approach to generate each row by calling itself with n-1 as the input.