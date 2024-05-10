
def pascal(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    rows = [[1], [1, 1]]
    if n == 2:
        return rows
    for i in range(2, n):
        prev_row = rows[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        rows.append(new_row)
    return rows
