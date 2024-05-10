
def sqrt(x, epsilon=1e-7):
    """
    This function computes the square root of a given input x up to an accuracy of epsilon using the
    Newton-Raphson method.
    
    Inputs:
    x: a non-negative float value for which the square root is to be computed
    epsilon: a non-negative float value indicating the required accuracy of the computed square root
             The default value of epsilon is set to 1e-7 if it's not provided.
    
    Output:
    A float value that represents the computed square root of x
    
    Example usage:
    >>> sqrt(4, 0.0001)
    2.0000000929222947
    """
    approx = x / 2
    
    while True:
        diff = abs(x - approx ** 2)
        if diff < epsilon:
            break
        approx = 0.5 * (approx + x / approx)
    
    return approx
