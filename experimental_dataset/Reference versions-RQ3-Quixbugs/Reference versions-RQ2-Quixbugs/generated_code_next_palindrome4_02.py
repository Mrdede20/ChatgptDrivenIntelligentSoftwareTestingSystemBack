
def create_next_palindrome(num):
    n = len(num)
    left = int(n / 2) - 1
    right = int(n / 2)
    increment = False

    while left >= 0 and right < n:
        if num[left] != num[right]:
            if num[left] < num[right]:
                increment = True
            num[right] = num[left]
        left -= 1
        right += 1
    
        if increment:
            carry = 1
            i = int(n / 2) - 1
            j = int(n / 2)
            while i >= 0 and j < n:
                temp = num[i] + carry
                num[i] = (temp) % 10
                num[j] = num[i]
                carry = int(temp / 10)
                i -= 1
                j += 1
            
            if carry > 0 and n % 2 != 0:
                num[int(n / 2)] += carry
            
            increment = False
    
    if all(i == 9 for i in num):
        num = [0] * (n + 1)
        num[0] = 1
        num[-1] = 1
    return num
