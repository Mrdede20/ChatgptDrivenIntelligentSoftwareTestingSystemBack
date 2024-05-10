
def sqrt(x, epsilon):
    """
    Takes two inputs- 'x' and 'epsilon' and returns the approximate square root of 'x' with a tolerance level of 'epsilon'.
    """
    assert x >= 1 and epsilon > 0

    approx = x
    while abs(approx**2 - x) > epsilon:
        approx = (approx + x/approx) / 2

    return approx
