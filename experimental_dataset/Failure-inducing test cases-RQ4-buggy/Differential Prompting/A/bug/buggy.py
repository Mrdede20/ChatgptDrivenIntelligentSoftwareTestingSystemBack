#https://codeforces.com/contest/1760/submission/182133676
t=int(input())
while t>1:
    for i in range(0,3):
        a=sorted(list(map(int,input().split())))
        print(a[1])
        t-=1