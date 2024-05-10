
def find_possible_paths(t: int, test_cases: list):
  for q in range(t):
    n, a, b = test_cases[q][:3]
    edges = test_cases[q][3:]
    graph = [[] for i in range(n+1)]
    
    for i in range(n-1):
      u, v, w = edges[i]
      graph[u].append((v, w))
      graph[v].append((u, w))

    visited_from_a = [False] * (n+1)
    visited_from_b = [False] * (n+1)

    def dfs(node, visited, target):
      nonlocal graph
      if node == target:
        return True
      visited[node] = True
      for neighbour, weight in graph[node]:
        if not visited[neighbour]:
          if dfs(neighbour, visited, target):
            return True
      
      return False

    has_common_path = False
    has_common_path = dfs(a, visited_from_a, b) and dfs(b, visited_from_b, a)
    if has_common_path:
      print("YES")
    else:
      print("NO")
      
    if q == 51:  # q is 0-indexed
      print(q+1)
      print(n, a, b)
      print(*edges)
