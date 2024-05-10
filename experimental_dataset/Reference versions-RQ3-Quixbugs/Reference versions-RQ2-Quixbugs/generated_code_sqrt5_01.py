
def calculate_sqrt(x, epsilon):
    approx = x/2
    while abs(approx**2 - x) > epsilon:
        approx = (approx + x/approx)/2
    return approx
