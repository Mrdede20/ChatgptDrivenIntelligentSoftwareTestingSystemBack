
def sort_and_print_middle(t: int) -> None:
    while t > 0:
        a, b, c = map(int, input().split())
        lst = [a, b, c]
        lst.sort()
        print(lst[1])
        t -= 1
