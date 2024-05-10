
def BinaryInversions(n, bits):
    first = 0
    second = 0
    for i in range(n-1):
        if bits[i] == 0 and bits[i+1] == 1:
            first += 1
    for i in range(n-2):
        if bits[i] == 0 and bits[i+1] == 1 and bits[i+2] == 0:
            second += 1
            bits[i] = 1
            bits[i+1] = 0
            bits[i+2] = 1
    max_inversions = first + second*2
    return max_inversions
