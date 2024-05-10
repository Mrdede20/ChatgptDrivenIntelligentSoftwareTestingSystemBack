
def next_palindrome(arr):
    """
    Returns the next palindrome array after arr
    """
    n=len(arr)
    mid=n//2
    left=False
    i=mid-1
    j=mid+1 if n%2 else mid
    while(i>=0 and arr[i]==arr[j])):
        i-=1
        j+=1
    if(i<0 or (arr[i]<arr[j] and not left))):
        left=True
    while(i>=0):
        arr[j]=arr[i]
        i-=1
        j+=1
    if(left):
        carry=1
        i=mid-1
        if n%2:
            arr[mid]+=carry
            carry=arr[mid]//10
            arr[mid]%=10
            j=mid+1
        else:
            j=mid
        while(i>=0):
            arr[i]+=carry
            carry=arr[i]//10
            arr[i]%=10
            arr[j]=arr[i]
            i-=1
            j+=1
    return arr
