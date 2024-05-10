
def pascal(n):
    if n == 1:
        return [[1]]
    else:
        rows = pascal(n-1)
        row = [1]
        for i in range(1, n-1):
            row.append(rows[-1][i-1] + rows[-1][i])
        row.append(1)
        rows.append(row)
        return rows
