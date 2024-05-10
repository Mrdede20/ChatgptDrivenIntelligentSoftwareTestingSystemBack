
def find_max_ascii(n: int) -> None:
    import string

    for i in range(n):
        a = int(input())
        s = input().strip()
        max_char = max(s.lower())
        result = string.ascii_lowercase.index(max_char) + 1
        print(result)
