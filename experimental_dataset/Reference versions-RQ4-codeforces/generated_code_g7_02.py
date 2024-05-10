
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

    def bfs(visited, queue, target):
      nonlocal graph
      while queue:
        node = queue.pop(0)
        for neighbour, weight in graph[node]:
          if not visited[neighbour]:
            visited[neighbour] = True
            if neighbour == target:
              return True
            queue.append(neighbour)
      return False

    queue_from_a = [a]
    queue_from_b = [b]
    visited_from_a[a] = True
    visited_from_b[b] = True

    has_common_path = False
    while queue_from_a or queue_from_b:
      if queue_from_a:
        if bfs(visited_from_a, queue_from_a, b):
          has_common_path = True
          break
      if queue_from_b:
        if bfs(visited_from_b, queue_from_b, a):
          has_common_path = True
          break
    
    if has_common_path:
      print("YES")
    else:
      print("NO")

    if q == 51:  # q is 0-indexed
      print(q+1)
      print(n, a, b)
      print(*edges)
