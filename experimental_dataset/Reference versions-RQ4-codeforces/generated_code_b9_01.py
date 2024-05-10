
def find_ascii_difference(n: int) -> None:
    for i in range(n):
        a, s = input().split()
        max_char = chr(ord('a')-1)
        for c in s:
            if ord(c) > ord(max_char) and ord(c) > int(a):
                max_char = c
        print(ord(max_char)-ord('a'))
