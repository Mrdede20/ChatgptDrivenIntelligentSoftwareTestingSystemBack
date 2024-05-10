
def max_integer_k(n, values):
    for i in range(n):
        lst = values[i][0]
        c = values[i][1]
        d = values[i][2]
        lst.sort(reverse=True)
        
        if sum(lst[:d]) >= c:
            print("Infinity")
        elif lst[0]*d < c:
            print("Impossible")
        else:
            low = d
            high = len(lst)
            while low < high:
                mid = (low + high) // 2
                if sum(lst[:mid]) >= c*d:
                    high = mid
                else:
                    low = mid + 1
            print(low-1)
