# Define function to check for valleys in a list
def has_valley(L):
    valleys = []
    for i in range(1, len(L)-1):
        if L[i] < L[i-1] and L[i] < L[i+1]:
            valleys.append(i)
    return len(valleys) == 1

# Define lambda functions to read input from standard input
ii = lambda: int(input().strip())
iilist = lambda: list(map(int, input().strip().split()))

# Read input and call has_valley on each list of numbers
t = ii()  # number of test cases
for _ in range(t):
    n = ii()  # length of list
    L = iilist()  # list of numbers
    if has_valley(L):
        print("YES")
    else:
        print("NO")
