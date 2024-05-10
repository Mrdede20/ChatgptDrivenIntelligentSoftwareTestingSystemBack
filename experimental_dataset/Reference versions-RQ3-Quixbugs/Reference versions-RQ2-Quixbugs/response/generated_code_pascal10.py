Sure, here are two versions of the program:

Version 1:

```python
def generate_pascals_triangle(n: int) -> list:
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
```

Version 2:

```python
def generate_pascals_triangle(n: int) -> list:
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(n-1)
        row = [1]
        for i in range(1, n-1):
            row.append(triangle[-1][i-1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)
        return triangle
```

Both functions take an integer `n` as input and return a list of `n` lists representing Pascal's Triangle. The first version uses a nested loop to generate each row of the triangle by adding up the values in the previous row. The second version uses recursion to generate the triangle by calling itself with `n-1` to generate the triangle up to the previous row and then leveraging the values in the last row to generate the current row.