Here are two programs that implement the Depth-first Search algorithm to determine if the goalnode is reachable from the startnode in a directed graph:

Program 1:

```
def dfs(startnode, goalnode):
    visited = set()

    def dfs_helper(current):
        visited.add(current)
        if current == goalnode:
            return True
        for neighbor in current.successors:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True
        return False

    return dfs_helper(startnode)
```

Program 2:

```
def dfs(startnode, goalnode):
    visited = set()
    stack = [startnode]

    while stack:
        current = stack.pop()
        
        if current == goalnode:
            return True
        
        visited.add(current)

        for neighbor in current.successors:
            if neighbor not in visited:
                stack.append(neighbor)

    return False
```

Both programs have the same method name `dfs` and the same parameter type of `startnode` and `goalnode`. They both implement the Depth-first Search algorithm to visit nodes and explore their successors until the goal node is found or all reachable nodes have been visited. 

Program 1 uses a recursive approach where a helper function is used to visit nodes and explore their successors until the goal node is found. The visited nodes are stored in a set to make sure each node is visited only once. Program 2 uses an iterative approach where a stack is used to keep track of nodes to be visited. The visited nodes are also stored in a set to ensure each node is visited only once. 

Both programs return a boolean value indicating whether the goalnode is reachable from the startnode.