
def find_largest_ascii(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_ascii = 0
        for char in s:
            if ord(char) > max_ascii:
                max_ascii = ord(char)
        if max_ascii > int(a) + 96:
            a = max_ascii - 96
        else:
            a = int(a)
        print(a)
