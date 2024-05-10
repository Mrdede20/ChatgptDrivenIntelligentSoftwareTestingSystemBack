Program 1:

```
def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        nodesvisited.add(node)
        if node == goalnode:
            return True
        return any(search_from(successor) for successor in node.successors)

    return search_from(startnode)
```

Program 2:

```
def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        nodesvisited.add(node)
        if node == goalnode:
            return True
        for successor in node.successors:
            if search_from(successor):
                return True
        return False

    return search_from(startnode)
``` 

Both the programs perform the same task of performing a depth-first search to determine if a certain goal node is reachable from a starting node in a directed graph. The difference is in the way they achieve the search. Program 1 uses the any() function to check if any of the successor nodes result in a successful search, whereas Program 2 uses a for loop to check each successor node one by one. Either program can be used based on personal preference or specific use case requirements.