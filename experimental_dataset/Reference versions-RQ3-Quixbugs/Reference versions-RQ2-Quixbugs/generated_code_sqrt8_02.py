
def sqrt(x, epsilon):
    approx = x/2
    difference = abs(x - approx**2)
    while difference > epsilon:
        approx = (approx + x/approx)/2
        difference = abs(x - approx**2)
    return approx
