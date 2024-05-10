
def find_max_ascii(n: int) -> None:
    for i in range(n):
        a = int(input())
        s = input().strip()
        max_ascii = max(ord(char) for char in s)
        result = max_ascii - 96
        print(result)
