Program 1: 

```
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited:
            if depth_first_search(successor, goal_node, visited):
                return True
    return False
```

Program 2: 

```
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node == goal_node:
            return True
        for successor in node.successors:
            if successor not in visited:
                visited.add(successor)
                stack.append(successor)
    return False
```

Both programs take a start node, a goal node, and a set of visited nodes (optional, with an empty set as the default). They use recursion or a stack-based approach to perform a depth-first search on the directed graph represented by the nodes. They maintain a set of visited nodes to avoid revisiting a node and potentially entering an infinite loop. Both programs return a boolean value indicating if the goal node is reachable from the start node.