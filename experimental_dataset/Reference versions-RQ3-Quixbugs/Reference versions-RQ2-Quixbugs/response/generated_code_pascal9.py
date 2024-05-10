Sure. Here are two Python programs that generate the first 'n' rows of Pascal's Triangle using a nested loop approach:

Method Name: `generate_pascals_triangle`
Parameter: integer `n`

Program 1:
```python
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
```

Program 2:
```python
def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
```

Both programs use a similar nested loop approach to generate the rows of Pascal's Triangle. Program 1 starts with an empty list and adds each row to it as it is generated, while Program 2 starts with the first row and builds the rest of the triangle from there.