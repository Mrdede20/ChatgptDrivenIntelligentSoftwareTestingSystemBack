
def newton_raphson_sqrt(x, epsilon):
    """
    Returns the approximated square root of 'x' with an error tolerance of 'epsilon' using Newton-Raphson method.
    
    Preconditions:
    - x >= 1
    - epsilon > 0
    """
    approx_sqrt = x/2
    while abs(approx_sqrt**2 - x) > epsilon:
        approx_sqrt = (approx_sqrt + x/approx_sqrt)/2
    return approx_sqrt
