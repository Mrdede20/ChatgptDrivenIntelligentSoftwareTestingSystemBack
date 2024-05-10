t = int(input())  # Number of test cases

while t > 0:
    a = sorted([int(x) for x in input().split()])  # Take 3 integer inputs and sort them
    print(a[1])  # Print the second (middle) number of the sorted sequence
    t -= 1  # Decrement t by 1 in each iteration
