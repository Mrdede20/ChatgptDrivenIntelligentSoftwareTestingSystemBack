
def sort_and_print_middle(t: int) -> None:
    for i in range(t):
        a, b, c = map(int, input().split())
        if b <= a <= c or c <= a <= b:
            print(a)
        elif a <= b <= c or c <= b <= a:
            print(b)
        else:
            print(c)
