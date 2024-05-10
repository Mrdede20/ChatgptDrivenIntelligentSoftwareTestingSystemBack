
def newton_raphson_sqrt(x, epsilon):
    """
    This function uses the Newton-Raphson method to approximate the square root of a given input value 'x' 
    with a certain level of accuracy determined by 'epsilon'. The function repeatedly updates the approximation 
    by calculating the average of it and the original value divided by the current approximation until the difference 
    between the approximation and the true square root calculated is below the specified level of accuracy. 
    The function returns the final approximation as the estimated square root of the original value.

    Args:
    x (float): Input value
    epsilon (float): Level of accuracy

    Returns:
    float: Estimated square root of the input value

    Example:
    >>> newton_raphson_sqrt(2, 0.01)
    1.4142156862745099
    """
    approx = x/2
    while True:
        better_approx = (approx + x/approx)/2
        if abs(better_approx - approx) < epsilon:
            return better_approx
        approx = better_approx
