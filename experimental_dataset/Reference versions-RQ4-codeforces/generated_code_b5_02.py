
def calculate_ascii(n):
    for i in range(n):
        s, num = input().split()
        max_ascii = max(list(map(ord, s)))
        result = max_ascii - 96
        print(result)
