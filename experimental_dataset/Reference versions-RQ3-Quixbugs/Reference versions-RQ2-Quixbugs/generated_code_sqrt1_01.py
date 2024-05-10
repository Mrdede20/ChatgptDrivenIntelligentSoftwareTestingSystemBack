
def newton_raphson_square_root(x, epsilon):
    approx = x / 2.0
    while True:
        better_approx = (approx + x / approx) / 2.0
        if abs(better_approx - approx) < epsilon:
            return better_approx
        approx = better_approx
