
def next_palindrome(arr):
    """
    Returns the next palindrome array after arr
    """
    n = len(arr)
    middle = n // 2
    left = False
    i = middle - 1
    j = middle + 1 if n%2 else middle
    while i >= 0 and arr[i] == arr[j]:
        i -= 1
        j += 1
    if i < 0 or arr[i] < arr[j]:
        left = True 
    while i >= 0:
        arr[j] = arr[i]
        j += 1
        i -= 1
    if left:
        carry = 1
        i = middle - 1
        if n%2:
            arr[middle] += carry
            carry = arr[middle] // 10
            arr[middle] %= 10
            j = middle + 1
        else:
            j = middle
        while i >= 0:
            arr[i] += carry
            carry = arr[i] // 10
            arr[i] %= 10
            arr[j] = arr[i]
            i -= 1
            j += 1
    return arr
