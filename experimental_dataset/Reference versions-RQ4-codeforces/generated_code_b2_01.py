
def largest_ascii(n):
    for i in range(n):
        a = int(input())
        s = input()
        max_ascii = a
        for char in s:
            if ord(char) > max_ascii:
                max_ascii = ord(char)
        print(max_ascii - 96)
