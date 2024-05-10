
def calculate_ascii(n):
    for i in range(n):
        s, num = input().split()
        max_ascii = 0
        for c in s:
            if ord(c) > max_ascii:
                max_ascii = ord(c)
        result = max_ascii - 96
        print(result)
