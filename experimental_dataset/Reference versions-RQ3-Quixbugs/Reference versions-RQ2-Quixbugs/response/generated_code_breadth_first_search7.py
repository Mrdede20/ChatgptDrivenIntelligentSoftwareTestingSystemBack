Sure, here are two versions of the function using different approaches -

Approach 1: Using a queue and a set of visited nodes

```
def bfs_search(start_node, goal_node):
    queue = [start_node]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node == goal_node:
            return True
        visited.add(node)
        for successor in node.successors:
            if successor not in visited:
                queue.append(successor)
    
    return False
```

Approach 2: Using a queue and a dictionary of node distances

```
def bfs_search(start_node, goal_node):
    queue = [start_node]
    distances = {start_node: 0}

    while queue:
        node = queue.pop(0)
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in distances:
                distances[successor] = distances[node] + 1
                queue.append(successor)
    
    return False
```

Note that both functions have the same name, parameter types, and achieve the same intention, but they use different data structures to keep track of visited nodes and node distances. The second approach adds a dictionary to keep track of the distance of each node from the starting node.