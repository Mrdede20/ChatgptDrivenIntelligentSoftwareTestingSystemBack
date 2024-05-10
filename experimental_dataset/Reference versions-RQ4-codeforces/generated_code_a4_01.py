
def find_median(t: int) -> None:
    # loop for t test cases
    for i in range(t):
        # input the three integers
        a, b, c = map(int, input().split())
        # sort the integers
        arr = sorted([a, b, c])
        # print the middle integer
        print(arr[1])
