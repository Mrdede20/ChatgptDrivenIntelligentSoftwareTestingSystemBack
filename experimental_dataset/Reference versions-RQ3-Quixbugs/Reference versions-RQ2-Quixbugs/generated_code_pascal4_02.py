
def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        rows = pascal(n - 1)
        prev_row = rows[-1]
        cur_row = [1] * n
        for i in range(1, n - 1):
            cur_row[i] = prev_row[i] + prev_row[i - 1]
        rows.append(cur_row)
        return rows
