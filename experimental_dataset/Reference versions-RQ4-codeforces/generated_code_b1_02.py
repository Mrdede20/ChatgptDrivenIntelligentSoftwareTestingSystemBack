
def find_max_unicode(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_unicode = max(map(ord, s))
        print(max_unicode-96)
