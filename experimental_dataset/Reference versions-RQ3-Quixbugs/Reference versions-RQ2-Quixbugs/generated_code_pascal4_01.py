
def pascal(n):
    if n <= 0:
        return []
    rows = [[1]]
    for i in range(1, n):
        prev_row = rows[-1]
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j] + prev_row[j - 1]
        rows.append(cur_row)
    return rows
