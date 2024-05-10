
def generate_pascals_triangle(n):
    """
    This function generates the first 'n' rows of Pascal's triangle.
    """
    rows = [[1]]  # Initialize rows list with the first row

    for i in range(2, n+1):
        row = [1]  # Every row starts with 1
        for j in range(1, i-1):
            row.append(rows[i-2][j-1] + rows[i-2][j])  # Calculate the left and right elements of the upper row
        row.append(1)  # Every row ends with 1
        rows.append(row)  # Append the row into the 'rows' list

    return rows
