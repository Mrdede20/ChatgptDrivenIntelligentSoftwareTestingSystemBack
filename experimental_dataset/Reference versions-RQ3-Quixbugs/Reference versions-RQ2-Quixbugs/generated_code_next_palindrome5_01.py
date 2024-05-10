
def next_palindrome(digit_list):
    n = len(digit_list)
    mid = n // 2
    i = mid - 1
    j = mid + 1 if n % 2 else mid

    while i >= 0 and digit_list[i] == digit_list[j]:
        i -= 1
        j += 1

    if i < 0 or digit_list[i] < digit_list[j]:
        carry = 1
        k = mid - 1
        if n % 2:
            digit_list[mid] += carry
            carry = digit_list[mid] // 10
            digit_list[mid] %= 10
            j = mid + 1
        else:
            j = mid

        while k >= 0:
            digit_list[k] += carry
            carry = digit_list[k] // 10
            digit_list[k] %= 10
            digit_list[j] = digit_list[k]
            k -= 1
            j += 1

    else:
        k = mid - 1
        j = mid + 1 if n % 2 else mid

        while k >= 0:
            digit_list[j] = digit_list[k]
            k -= 1
            j += 1

    return digit_list
