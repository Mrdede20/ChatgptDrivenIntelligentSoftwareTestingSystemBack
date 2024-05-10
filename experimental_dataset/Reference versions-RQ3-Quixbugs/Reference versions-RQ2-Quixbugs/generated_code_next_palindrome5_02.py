
def next_palindrome(digit_list):
    n = len(digit_list)
    mid = n // 2
    left = mid - 1
    right = mid + 1 if n % 2 == 1 else mid

    while left >= 0 and digit_list[left] == digit_list[right]:
        left -= 1
        right += 1

    if left < 0:
        digit_list = [1] + [0] * (n - 1)
    elif digit_list[left] < digit_list[right]:
        digit_list[left] += 1
        for i in range(left+1,mid):
            digit_list[i] = digit_list[left]
        if n%2 == 1:
            digit_list[mid] = digit_list[left]
    else:
        for i in range(left+1,mid):
            digit_list[i] = digit_list[left-i+mid]
        if n%2 == 1:
            digit_list[mid] = digit_list[mid-1]

    return digit_list
