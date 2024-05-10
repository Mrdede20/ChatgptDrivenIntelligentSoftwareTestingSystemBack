n = int(input())

for i in range(n):
    a = input()
    s = input()
    max_ascii = 0
    for c in s:
        ascii_value = ord(c)
        if ascii_value > max_ascii:
            max_ascii = ascii_value
    result = max_ascii - 96
    print(result)