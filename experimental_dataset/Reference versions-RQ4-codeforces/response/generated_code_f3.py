Program 1:
```python
def calculate(n, c, d, A):
    for i in range(n):
        A.sort(reverse=True)
        if sum(A[:d]) >= c:
            print("Infinity")
        elif A[0]*d < c:
            print("Impossible")
        else:
            low = 0
            high = len(A) - 1
            while low <= high:
                mid = (low + high) // 2
                if sum(A[:mid]) + A[mid]*(d-1) >= c:
                    high = mid - 1
                else:
                    low = mid + 1
            print(mid)
```

Program 2:
```python
def calculate(n, c, d, A):
    for i in range(n):
        A.sort(reverse=True)
        if sum(A[:d]) >= c:
            print("Infinity")
        elif A[0]*d < c:
            print("Impossible")
        else:
            low = 0
            high = len(A) - 1
            while low <= high:
                mid = (low + high) // 2
                total_cost = 0
                for j in range(mid):
                    total_cost += A[j]
                total_cost += A[mid] * (d-1)
                if total_cost >= c:
                    high = mid - 1
                else:
                    low = mid + 1
            print(mid)
```