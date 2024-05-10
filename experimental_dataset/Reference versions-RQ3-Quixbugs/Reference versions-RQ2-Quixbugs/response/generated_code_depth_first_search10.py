Program 1:

```python
def depth_first_search(start_node, goal_node, visited_nodes=set()):
    visited_nodes.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited_nodes:
            if depth_first_search(successor, goal_node, visited_nodes):
                return True
    return False
```

Program 2:

```python
def depth_first_search(start_node, goal_node):
    visited_nodes = set()
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node == goal_node:
            return True
        visited_nodes.add(current_node)
        for successor in current_node.successors:
            if successor not in visited_nodes:
                stack.append(successor)
    return False
```

Both programs implement depth-first search to find if a goal node is reachable from a start node in a directed graph. The first program is a recursive implementation while the second program uses a stack to perform the search iteratively. In both programs, a set of visited nodes is maintained to keep track of nodes that have already been explored to avoid revisiting them.