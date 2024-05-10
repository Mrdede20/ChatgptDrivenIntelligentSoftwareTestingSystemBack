
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
