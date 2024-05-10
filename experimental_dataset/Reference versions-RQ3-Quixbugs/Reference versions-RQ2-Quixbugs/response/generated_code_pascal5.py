Program 1:
```python
def pascal(n):
    """
    Function to generate first n rows of Pascal's Triangle
    """
    triangle = []
    for row in range(n):
        triangle.append([1]*(row+1))
        for col in range(1, row):
            triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]
    return triangle
```

Program 2:
```python
def pascal(n):
    """
    Function to generate first n rows of Pascal's Triangle
    """
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    triangle = pascal(n-1)
    last_row = triangle[-1]
    row = [1]
    for i in range(len(last_row)-1):
        row.append(last_row[i]+last_row[i+1])
    row.append(1)
    triangle.append(row)
    return triangle
```

Both programs have the same method name `pascal()` and the same parameter type `n`.