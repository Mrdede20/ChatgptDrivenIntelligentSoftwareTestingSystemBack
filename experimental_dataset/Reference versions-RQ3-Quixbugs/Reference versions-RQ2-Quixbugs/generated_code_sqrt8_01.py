
def sqrt(x, epsilon):
    approx = x/2
    while abs(x - approx**2) > epsilon:
        approx = (approx + x/approx)/2
    return approx
