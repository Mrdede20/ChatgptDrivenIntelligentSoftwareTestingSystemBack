
def print_second_smallest(t):
    while t > 0:
        a, b, c = map(int, input().split())
        if a > b:
            if c > b:
                print(c)
            elif a > c:
                print(a)
            else:
                print(c)
        else:
            if c > a:
                print(c)
            elif b > c:
                print(b)
            else:
                print(c)
        t -= 1
