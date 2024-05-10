x = int(input())
while x>0:
    a=sorted(list(map(int, input().split())))
    print(a[1])
    x-=1