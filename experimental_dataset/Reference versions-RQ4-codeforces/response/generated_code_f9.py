Here are the two programs that solve the given problem:

Program 1: Using Binary Search

```python
def select_numbers(n, c, d, a):
    low, high, ans = 0, n, 0
    
    def feasible(mid):
        groups = [a[i:i+mid] for i in range(n-mid+1)] # Create groups of mid consecutive numbers
        cost = sum(max(group) for group in groups) # Calculate maximum number from each group and add them
        return cost <= c # Check if total cost is less than or equal to c
    
    while low <= high:
        mid = (low+high)//2 # Calculate mid
        if feasible(mid):
            ans = mid # Update answer
            low = mid+1 # Search for larger mid values
        else:
            high = mid-1 # Search for smaller mid values
    
    if ans == 0: # If no value of mid is feasible, return "Impossible"
        return "Impossible"
    elif ans*d <= n: # If mid values can be selected d times and still there are enough elements in A, return ans
        return ans
    else: # Otherwise, return "Infinity"
        return "Infinity"
```

Program 2: Using Brute Force

```python
def select_numbers(n, c, d, a):
    ans = 0
    
    def feasible(mid):
        groups = [a[i:i+mid] for i in range(n-mid+1)] # Create groups of mid consecutive numbers
        cost = sum(max(group) for group in groups) # Calculate maximum number from each group and add them
        return cost <= c # Check if total cost is less than or equal to c
    
    for mid in range(1, n+1):
        if feasible(mid):
            ans = mid # Update answer
    
    if ans == 0: # If no value of mid is feasible, return "Impossible"
        return "Impossible"
    elif ans*d <= n: # If mid values can be selected d times and still there are enough elements in A, return ans
        return ans
    else: # Otherwise, return "Infinity"
        return "Infinity"
```