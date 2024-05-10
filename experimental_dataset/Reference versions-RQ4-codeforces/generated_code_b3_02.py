
def find_largest_ascii(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_ascii = ord(max(s))
        if max_ascii > int(a) + 96:
            a = max_ascii - 96
        else:
            a = int(a)
        print(a)
