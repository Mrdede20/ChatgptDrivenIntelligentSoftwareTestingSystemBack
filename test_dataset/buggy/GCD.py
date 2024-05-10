def gcd1 (a, b) :
    if b == 0 :
        return a
    else :
        return gcd1 (a, a%b)


a = int(input())
b = int(input())
print(gcd1(a,b))