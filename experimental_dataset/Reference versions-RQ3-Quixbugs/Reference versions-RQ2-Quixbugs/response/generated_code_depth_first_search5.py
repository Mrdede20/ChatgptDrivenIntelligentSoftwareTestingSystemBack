Sure, here are the two programs:

Program 1: 

```
def search_from(start_node, goal_node, visited_set=set()):
    visited_set.add(start_node)
    if start_node == goal_node:
        return True
    for successor in start_node.successors:
        if successor not in visited_set:
            if search_from(successor, goal_node, visited_set):
                return True
    return False
```

Program 2:

```
def search_from(start_node, goal_node, visited_set=set()):
    visited_set.add(start_node)
    for successor in start_node.successors:
        if successor not in visited_set:
            if successor == goal_node or search_from(successor, goal_node, visited_set):
                return True
    return False
```

Both programs essentially do the same thing, but Program 2 combines the base case of whether the start node is the goal node with the recursive case of checking the successors. 

To use either program, simply call the `search_from` function with the start node and goal node as parameters, like this:

```
start_node = Node(value=1, successors=[Node(value=2), Node(value=3)])
goal_node = Node(value=4)
result = search_from(start_node, goal_node)
```

In this example, the DFS algorithm will search for a path from `start_node` to `goal_node` through the successor nodes defined in the `Node` objects. The function will return `True` if a path exists and `False` otherwise.