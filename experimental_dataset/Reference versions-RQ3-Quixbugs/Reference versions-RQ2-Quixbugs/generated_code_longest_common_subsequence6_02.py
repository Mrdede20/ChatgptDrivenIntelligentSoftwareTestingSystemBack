
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
