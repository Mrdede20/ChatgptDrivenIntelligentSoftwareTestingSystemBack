
def print_middle_integer(t:int):
    for i in range(t):
        lst = list(map(int, input().split()))
        lst.sort()
        print(lst[1])
