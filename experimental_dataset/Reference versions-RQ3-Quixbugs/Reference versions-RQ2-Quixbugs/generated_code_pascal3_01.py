
def pascal(n):
    rows = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(rows[i-1][j-1] + rows[i-1][j])
        row.append(1)
        rows.append(row)
    return rows
