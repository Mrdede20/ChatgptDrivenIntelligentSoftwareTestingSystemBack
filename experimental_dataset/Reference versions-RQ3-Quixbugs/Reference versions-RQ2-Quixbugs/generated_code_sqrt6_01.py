
def newton_raphson_sqrt(x, epsilon):
    approx_root = x / 2
    while abs(approx_root**2 - x) > epsilon:
        approx_root = (approx_root + x / approx_root) / 2
    return approx_root
