Here are two programs that achieve the same intention: 

Program 1:

```
def solve(heights):
    max_height = max(heights)
    if heights.count(max_height) == 1:
        return True
    else:
        return False
     
     
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        heights = list(map(int, input().split()))
        result = solve(heights)
        if result:
            print("YES")
        else:
            print("NO")
```

Program 2:

```
def solve(heights):
    max_height = max(heights)
    winner_count = 0
    for height in heights:
        if height == max_height:
            winner_count += 1
            if winner_count > 1:
                return False
    return True


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        heights = list(map(int, input().split()))
        result = solve(heights)
        if result:
            print("YES")
        else:
            print("NO")
```

Both programs have the same method name `solve` and the same parameter type - a list of integers (heights of children). The programs first take input in the specified format and then call the `solve()` function for each test case. The `solve()` function returns True if there is only one winner and False if there are multiple winners. The main program then outputs YES if there is one winner and NO if there are multiple winners.