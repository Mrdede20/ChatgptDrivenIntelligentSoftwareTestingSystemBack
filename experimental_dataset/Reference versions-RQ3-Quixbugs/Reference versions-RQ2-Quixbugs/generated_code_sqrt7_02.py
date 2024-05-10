
def sqrt(x, epsilon, approx=None):
    """
    Takes two inputs- 'x' and 'epsilon' and returns the approximate square root of 'x' with a tolerance level of 'epsilon'.
    """
    assert x >= 1 and epsilon > 0

    if approx == None:
        approx = x

    if abs(approx**2 - x) <= epsilon:
        return approx
    else:
        return sqrt(x, epsilon, (approx + x/approx) / 2)
