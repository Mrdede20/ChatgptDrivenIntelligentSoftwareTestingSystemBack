
import math

def calculate_sqrt(x, epsilon):
    approx = x/2
    while not math.isclose(approx**2, x, rel_tol=epsilon):
        approx = (approx + x/approx)/2
    return approx
