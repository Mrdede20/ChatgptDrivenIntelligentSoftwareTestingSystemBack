
def newton_raphson_sqrt(x, epsilon):
    approx_root = x / 2
    diff = abs(approx_root**2 - x)
    while diff > epsilon:
        approx_root = (approx_root + x / approx_root) / 2
        diff = abs(approx_root**2 - x)
    return approx_root
