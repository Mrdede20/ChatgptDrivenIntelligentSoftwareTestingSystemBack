
def newton_raphson_square_root(x, epsilon):
    approx = x / 2.0
    difference = abs(x - approx**2)
    while difference > epsilon:
        approx = (approx + x / approx) / 2.0
        difference = abs(x - approx**2)
    return approx
