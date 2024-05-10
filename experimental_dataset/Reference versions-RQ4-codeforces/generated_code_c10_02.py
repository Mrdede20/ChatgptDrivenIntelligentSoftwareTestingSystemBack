
def max_difference(t, n, s):
    for i in range(t):
        s[i].sort(reverse=True)
        max1 = s[i][0]
        max2 = s[i][1]
        for num in s[i]:
            if num == max1:
                print(max1 - max2)
            else:
                print(max1 - num)
