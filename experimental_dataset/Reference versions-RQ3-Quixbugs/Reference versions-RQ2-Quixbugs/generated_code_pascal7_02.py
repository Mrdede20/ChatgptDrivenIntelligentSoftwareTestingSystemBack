
def generate_pascals_triangle(n):
    """
    This function generates the first 'n' rows of Pascal's triangle.
    """
    rows = [[1]]  # Initialize rows list with the first row

    for i in range(2, n+1):
        row = [1] * i  # Every row starts and ends with 1
        for j in range(1, i-1):
            row[j] = rows[i-2][j-1] + rows[i-2][j]  # Calculate the left and right elements of the upper row
        rows.append(row)  # Append the row into the 'rows' list

    return rows
