
import statistics

def find_median(t: int) -> None:
    # loop for t test cases
    for i in range(t):
        # input the three integers
        a, b, c = map(int, input().split())
        # calculate the median
        median = statistics.median([a, b, c])
        # print the median
        print(median)
