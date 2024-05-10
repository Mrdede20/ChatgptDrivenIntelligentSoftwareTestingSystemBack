
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
