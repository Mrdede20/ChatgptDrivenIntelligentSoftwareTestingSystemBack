Here are two programs that achieve the intended purpose:

Program 1:

```python
def generate_pascals_triangle(n):
    if n == 1:
        return [[1]]
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
```

Program 2:

```python
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
```

Both of these programs take an integer `n` as input and return a list of n lists representing the first n rows of Pascal's triangle. The first program uses nested for loops to iteratively compute each row of the triangle, while the second program uses a slightly more concise approach that checks whether each element is on the edge (i.e. has a value of 1) or needs to be summed with the two elements above and to its left and right.