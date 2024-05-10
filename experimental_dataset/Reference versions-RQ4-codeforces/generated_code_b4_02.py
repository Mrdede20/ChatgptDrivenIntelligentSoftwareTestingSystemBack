
def ascii_position(n):
    for i in range(n):
        a, s = input().split()
        a = int(a)
        max_char = chr(a)
        for i in range(len(s)):
            if ord(s[i]) > a and ord(s[i]) > ord(max_char):
                max_char = s[i]
        print(ord(max_char) - 96)
