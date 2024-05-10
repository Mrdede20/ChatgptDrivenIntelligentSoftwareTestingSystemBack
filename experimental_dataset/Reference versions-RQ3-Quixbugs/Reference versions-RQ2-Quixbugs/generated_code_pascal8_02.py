
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
