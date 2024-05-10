
def two_paths(t: int, n: int, a: int, b: int, edges: list) -> None:
    def dfs(x, parent, path, fromA, fromB):
        path ^= edges[parent][x]
        if parent == a:
            fromA[x] = path
        elif parent == b:
            fromB[x] = path
        for y in edges[x]:
            if y != parent:
                dfs(y, x, path, fromA, fromB)
    
    for _ in range(t):
        edges = [{} for _ in range(n+1)]
        for i in range(n-1):
            u, v, w = map(int, input().split())
            edges[u][v] = w
            edges[v][u] = w
        
        fromA = [0] * (n+1)
        fromB = [0] * (n+1)
        dfs(a, 0, 0, fromA, fromB)
        
        if any([(fromA[x] ^ fromB[x]) > 0 for x in range(1, n+1)]):
            print("YES")
        elif fromB.count(0) > 2:
            print("YES")
        else:
            print("NO")
