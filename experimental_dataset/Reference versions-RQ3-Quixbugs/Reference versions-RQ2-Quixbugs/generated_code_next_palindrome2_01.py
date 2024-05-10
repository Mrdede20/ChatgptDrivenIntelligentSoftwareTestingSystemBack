
def next_palindrome(digits):
    n = len(digits)
    if n == 1:
        return [digits[0]+1]
    elif n % 2 == 0:
        left_middle = n//2 -1
        right_middle = n//2
    else:
        left_middle = right_middle = n//2
    i = left_middle
    j = right_middle
    while i >= 0 and j < n and digits[i] == digits[j]:
        i -= 1
        j += 1
    if i < 0 or digits[i] < digits[j]:
        carry = 1
        i = left_middle
        j = right_middle
        while i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            digits[j] = digits[i]
            i -= 1
            j += 1
    else:
        i = left_middle
        j = right_middle
        while i >= 0:
            digits[j] = digits[i]
            i -= 1
            j += 1
    if carry:
        return [1] + [0] * (n-1) + [1]
    else:
        return digits
