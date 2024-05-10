Program 1:

```
def depth_first_search(start_node, goal_node):
    
    def search_from(current_node, visited):
        visited.add(current_node)
        
        if current_node == goal_node:
            return True
        
        for successor in current_node.successors:
            if successor not in visited:
                if search_from(successor, visited):
                    return True
        
        return False
    
    nodesvisited = set()
    return search_from(start_node, nodesvisited)
```

Program 2:

```
def depth_first_search(start_node, goal_node):
    
    def search_from(current_node, visited):
        visited.add(current_node)
        
        if current_node == goal_node:
            return True
        
        for successor in current_node.successors:
            if successor not in visited:
                if search_from(successor, visited):
                    return True
        
        return False
    
    nodesvisited = set()
    return search_from(start_node, nodesvisited)
```

Both programs implement the Depth First Search algorithm to determine if a goal node is reachable from a starting node in a directed graph, using the same nested function `search_from()` to perform the recursive search and keeping track of the visited nodes in a set `nodesvisited`. The function returns `True` if the goal node is reachable from the starting node, otherwise `False`.