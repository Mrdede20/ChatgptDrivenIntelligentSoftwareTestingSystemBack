Sure, here are two programs that generate the first n rows of Pascal's Triangle using the same method name and same parameter type:

Program 1:
```python
def pascals_triangle(n: int) -> List[List[int]]:
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle[:n]
```
Program 2:
```python
from typing import List

def pascals_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    
    triangle = pascals_triangle(n-1)
    last_row = triangle[-1]
    row = [1]
    
    for i in range(1, len(last_row)):
        row.append(last_row[i-1] + last_row[i])
    
    row.append(1)
    triangle.append(row)
    
    return triangle
```

Both programs take an integer n as input and return a list of lists representing the first n rows of Pascal's Triangle. The first program uses a nested for loop to generate each row of the triangle iteratively, while the second program recursively calls itself to return the previous rows of the triangle and then generates the new row based on the previous row.