
def find_ascii_difference(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_char = max([c for c in s if ord(c) > int(a)], default='a')
        print(ord(max_char)-ord('a'))
