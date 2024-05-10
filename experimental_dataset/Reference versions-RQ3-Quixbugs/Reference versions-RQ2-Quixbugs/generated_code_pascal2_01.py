
def pascal(n):
    """
    This function generates the first n rows of Pascal's triangle.
    The resulting triangle is represented as a list of n lists, where each inner list represents a row in the triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
