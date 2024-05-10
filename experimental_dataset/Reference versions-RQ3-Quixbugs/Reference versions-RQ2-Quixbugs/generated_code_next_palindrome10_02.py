
def next_palindrome(arr):
    n = len(arr)
    mid = n // 2
    left = False
    
    if n % 2 == 0:
        left = True
        
    while mid >= 0 and mid < n:
        if arr[mid] < 9:
            arr[mid] += 1
            if mid != n - mid - 1:
                arr[n - mid - 1] += 1
            break
        arr[mid] = arr[n - mid - 1] = 0
        mid -= 1
        
        if mid < 0:
            if not left:
                mid = n // 2
            else:
                mid = (n // 2) - 1
            carry = 1
            i = mid
            while i >= 0:
                arr[i] += carry
                carry = arr[i] // 10
                arr[i] %= 10
                arr[n - i - 1] = arr[i]
                i -= 1
    return arr
