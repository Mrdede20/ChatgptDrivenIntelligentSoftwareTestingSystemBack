
def ascii_position(n):
    a = 0
    for i in range(n):
        a=int(input())
        s=input()
        max_char = chr(a)
        for i in range(len(s)):
            if ord(s[i]) > a and ord(s[i]) > ord(max_char):
                max_char = s[i]
        print(ord(max_char) - 96)
