Here are two programs that achieve the intention using recursion:

Program 1:

```
def findLCS(a:str,b:str) -> str:
    if len(a)==0 or len(b)==0:
        return ""
    elif a[0]==b[0]:
        return a[0]+findLCS(a[1:],b[1:])
    else:
        return max(findLCS(a[1:], b), findLCS(a, b[1:]), key=len)

#Testing the function
a = "AGGTAB"
b = "GXTXAYB"
print("LCS of",a,"and",b,"is",findLCS(a,b)) #Output: LCS of AGGTAB and GXTXAYB is GTAB
```

Program 2:

```
def findLCS(a:str,b:str) -> str:
    def LCS(i,j):
        if i==len(a) or j==len(b):
            return ""
        elif a[i]==b[j]:
            return a[i]+LCS(i+1,j+1)
        else:
            return max(LCS(i+1,j), LCS(i,j+1), key=len)
    return LCS(0,0)

#Testing the function
a = "AGGTAB"
b = "GXTXAYB"
print("LCS of",a,"and",b,"is",findLCS(a,b)) #Output: LCS of AGGTAB and GXTXAYB is GTAB
```

Both programs have the same method name and parameter type as required. Program 2 contains an inner recursive function `LCS()` to encapsulate the recursion logic. Program 1 uses if-elif-else statements in the main function to handle the recursion. Both programs return the LCS of characters between two given input strings.