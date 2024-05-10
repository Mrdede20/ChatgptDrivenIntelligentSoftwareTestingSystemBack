
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
            k = 0
            for j in range(d, len(lst)+1):
                if sum(lst[:j]) >= c*d:
                    k = j
            print(k-1)
