Program 1:

```
class DepthFirstSearch:
    def __init__(self, start_node, goal_node):
        self.visited = set()
        self.start_node = start_node
        self.goal_node = goal_node

    def dfs(self, current_node):
        if current_node == self.goal_node:
            return True
        if current_node in self.visited:
            return False
        self.visited.add(current_node)
        for successor in current_node.successors:
            if self.dfs(successor):
                return True
        return False

    def search(self):
        return self.dfs(self.start_node)
```

Program 2:

```
def depth_first_search(start_node, goal_node):
    visited = set()
    def dfs(current_node):
        if current_node == goal_node:
            return True
        if current_node in visited:
            return False
        visited.add(current_node)
        for successor in current_node.successors:
            if dfs(successor):
                return True
        return False

    return dfs(start_node)
```


Both programs use the Depth-first Search algorithm to search for the goal node starting from the start node of a directed graph. The algorithm keeps track of the nodes visited to avoid visiting the same node more than once. The output of the function is a boolean value that reflects whether the goal node is reachable from the start node. The first program is implemented as a class and the second program is implemented as a function.