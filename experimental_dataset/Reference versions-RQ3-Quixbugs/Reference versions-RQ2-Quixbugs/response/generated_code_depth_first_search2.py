Sure, here are two programs that accomplish the given task using depth-first search algorithm using the same method name and parameter type:

Program 1:
```
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    if start_node == goal_node:
        return True
    for node in start_node.successors:
        if node not in visited:
            if depth_first_search(node, goal_node, visited):
                return True
    return False
```

Program 2:
```
def depth_first_search(start_node, goal_node, visited=set()):
    visited.add(start_node)
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node == goal_node:
            return True
        for node in current_node.successors:
            if node not in visited:
                visited.add(node)
                stack.append(node)
    return False
``` 

In both programs, the `depth_first_search` function takes in a `start_node` and a `goal_node`. The `visited` set is used to keep track of which nodes have been visited during the search. The first program uses recursion to traverse the graph, while the second program uses a stack to keep track of the nodes to visit. Both programs explore each potential path as far as possible before backtracking, while maintaining a set of visited nodes to avoid revisiting nodes that have already been explored. 

Let us know if you have further questions!