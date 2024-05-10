Sure, here are two programs using the Depth-first Search algorithm to determine if a goal node is reachable from a starting node in a directed graph:

Program 1:

```
def dfs_search(start_node, goal_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node == goal_node:
            return True
        visited.add(node)
        for successor in node.successors:
            if successor not in visited:
                stack.append(successor)
                
    return False
```

Program 2:

```
def dfs_search(start_node, goal_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    
    if start_node == goal_node:
        return True
    
    for successor in start_node.successors:
        if successor not in visited:
            found = dfs_search(successor, goal_node, visited)
            if found:
                return True
    
    return False
```

Both programs use a depth-first search algorithm to traverse the graph and check if the goal node is reachable from the given start node. Program 1 uses an iterative approach with a stack, while Program 2 uses a recursive approach.