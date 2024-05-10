
def print_second_smallest(t):
    for i in range(t):
        lst = list(map(int, input().split()))
        lst.remove(max(lst))
        print(min(lst))
