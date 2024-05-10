
def newton_raphson_sqrt(x, epsilon):
    """
    Returns the approximated square root of 'x' with an error tolerance of 'epsilon' using Newton-Raphson method.
    
    Preconditions:
    - x >= 1
    - epsilon > 0
    """
    approx_sqrt = x/2
    diff = abs(approx_sqrt**2 - x)
    while diff > epsilon:
        approx_sqrt = (approx_sqrt + x/approx_sqrt)/2
        diff = abs(approx_sqrt**2 - x)
    return approx_sqrt
