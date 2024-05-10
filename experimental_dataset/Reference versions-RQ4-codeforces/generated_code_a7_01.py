
def second_largest(t: int) -> None:
    for i in range(t):
        a, b, c = sorted(map(int, input().split()))
        print(b)
