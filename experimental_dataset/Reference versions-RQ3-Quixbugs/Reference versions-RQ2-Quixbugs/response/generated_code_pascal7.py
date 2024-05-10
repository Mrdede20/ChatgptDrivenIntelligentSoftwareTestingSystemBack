Here are two programs that generate the first 'n' rows of Pascal's Triangle:

Program 1:

```python
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
```

Program 2:

```python
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
```

Both programs have the same method name `generate_pascals_triangle` and parameter type `n`. The difference between the two programs is in the way they handle the left and right elements of the upper row. Program 1 appends the left and right elements to the new row, while Program 2 initializes the new row with 1s and updates the middle elements of the row with the left and right elements of the upper row.