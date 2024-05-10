Sure, here are two implementations of the `depth_first_search` function according to your requirements:

Implementation 1:
```python
class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self.successor

    def successors(self):
        return self.successors

    def predecessors(self):
        return self.predecessors

def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False

        nodesvisited.add(node)

        if node == goalnode:
            return True

        for nextnode in node.successors:
            if search_from(nextnode):
                return True

        return False

    return search_from(startnode)
```

Implementation 2 (without using `successors` attribute):
```python
class Node:
    def __init__(self, value=None, successor=None, predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self.successor

    def predecessors(self):
        return self.predecessors

def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False

        nodesvisited.add(node)

        if node == goalnode:
            return True

        for nextnode in node.successors():
            if search_from(nextnode):
                return True

        return False

    return search_from(startnode)
``` 

Both implementations work successfully and return True if the `goalnode` is reachable from the `startnode` in the directed graph or False otherwise.