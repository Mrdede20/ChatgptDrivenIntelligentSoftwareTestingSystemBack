Program 1:

```
def find_path(t: int, test_cases: List[List[int]]) -> None:
    """
    This function takes an integer t and a list of test cases. Each test case is a list of three integers: n, a, and b.
    Using the edges list, the function creates a dictionary of dictionaries called 'edges', contains the list of vertices and its corresponding edges.
    The function searches the distance of all its edges from starting point to all other vertices and store in the fromA list.
    It searches the distance of all its edges from the end point to all other vertices and store them in fromB list.
    Then, it compares the fromA and fromB lists to decide whether there exists a path or not. If either one of the conditions is True, then it prints YES, else it prints NO.
    """
    for i in range(t):
        n, a, b = test_cases[i]
        edges = {}
        for j in range(n):
            edges[j+1] = {}
        for j in range(n-1):
            u, v, w = map(int, input().split())
            edges[u][v] = w
            edges[v][u] = w
        fromA = {a: 0}
        q = [a]
        visited = set()
        while q:
            x = q.pop(0)
            visited.add(x)
            for y in edges[x]:
                if y not in visited:
                    q.append(y)
                    fromA[y] = fromA[x] + edges[x][y]
        fromB = {b: 0}
        q = [b]
        visited = set()
        while q:
            x = q.pop(0)
            visited.add(x)
            for y in edges[x]:
                if y not in visited:
                    q.append(y)
                    fromB[y] = fromB[x] + edges[x][y]
        if fromA[b] == fromB[a]:
            print("YES")
        else:
            print("NO")
```

Program 2:

```
def find_path(t: int, test_cases: List[List[int]]) -> None:
    """
    This function takes an integer t and a list of test cases. Each test case is a list of three integers: n, a, and b.
    Using the edges list, the function creates a dictionary of dictionaries called 'edges', contains the list of vertices and its corresponding edges.
    The function searches the distance of all its edges from starting point to all other vertices and store in the fromA list.
    It searches the distance of all its edges from the end point to all other vertices and store them in fromB list.
    Then, it compares the fromA and fromB lists to decide whether there exists a path or not. If either one of the conditions is True, then it prints YES, else it prints NO.
    """
    for i in range(t):
        n, a, b = test_cases[i]
        edges = {}
        for j in range(n):
            edges[j+1] = {}
        for j in range(n-1):
            u, v, w = map(int, input().split())
            edges[u][v] = w
            edges[v][u] = w
        fromA = {a: 0}
        q = [a]
        visited = set()
        while q:
            x = q.pop(0)
            visited.add(x)
            for y in edges[x]:
                if y not in visited:
                    q.append(y)
                    fromA[y] = fromA[x] + edges[x][y]
        fromB = {b: 0}
        q = [b]
        visited = set()
        while q:
            x = q.pop(0)
            visited.add(x)
            for y in edges[x]:
                if y not in visited:
                    q.append(y)
                    fromB[y] = fromB[x] + edges[x][y]
        if fromA[b] == fromB[a]:
            print("YES")
        else:
            print("NO")
```