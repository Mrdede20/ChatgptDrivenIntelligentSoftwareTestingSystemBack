
n=int(input())

for i in range(n):
            b=0
            a=int(input())
            s=input()
            for i in range(len(s)):
                        if ord(s[i])>b:
                                    b=ord(s[i])
            print(b-96)

            