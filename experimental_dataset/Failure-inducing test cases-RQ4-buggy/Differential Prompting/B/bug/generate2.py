n = int(input())

for i in range(n):
    a=int(input())
    s=input()
    max_ascii = max([ord(c) for c in s])
    print(max_ascii - 96)
