def gcd2 (a, b) :
    if b == 0 :
        return a
    else :
        return gcd2 (b,a%b)


a = int(input())
b = int(input())
print(gcd2(a, b))