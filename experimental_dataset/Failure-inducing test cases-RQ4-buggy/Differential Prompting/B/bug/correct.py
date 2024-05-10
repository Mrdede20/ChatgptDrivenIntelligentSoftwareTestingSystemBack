s='abcdefghijklmnopqrstuvwxyz'
n=int(input())
i=0
while i<n:
    v=int(input())
    s2=input()
    z=0
    l=0
    for x in s2:
        z=(s.find(x)+1)
        if z>l:
            l=z
        else:
            continue
    print(l)
    i+=1
