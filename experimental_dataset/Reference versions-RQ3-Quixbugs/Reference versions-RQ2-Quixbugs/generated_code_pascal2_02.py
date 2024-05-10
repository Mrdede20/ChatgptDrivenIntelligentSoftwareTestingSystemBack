
def pascal(n):
    """
    This function generates the first n rows of Pascal's triangle.
    The resulting triangle is represented as a list of n lists, where each inner list represents a row in the triangle.
    """
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]
        for j in range(1, i):
            next_row.append(prev_row[j-1] + prev_row[j])
        next_row.append(1)
        triangle.append(next_row)
    return triangle
