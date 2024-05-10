
def find_max_unicode(n: int) -> None:
    for i in range(n):
        a, s = map(str,input().split())
        max_unicode = 0
        for j in range(len(s)):
            if ord(s[j]) > max_unicode:
                max_unicode = ord(s[j])
        print(max_unicode-96)
