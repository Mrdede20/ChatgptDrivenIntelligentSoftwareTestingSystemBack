
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
