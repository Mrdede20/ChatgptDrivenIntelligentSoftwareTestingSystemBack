Here are two solutions, one using a hash table to keep track of visited nodes, and the other using the tortoise-and-hare method:

Using Hash Table:

```python
def has_cycle(head: Node) -> bool:
    visited = {}
    curr = head
    while curr:
        if curr in visited:
            return True
        visited[curr] = True
        curr = curr.successor
    return False
```

Using Tortoise-and-Hare Method:

```python
def has_cycle(head: Node) -> bool:
    tortoise = head
    hare = head
    while hare and hare.successor:
        hare = hare.successor.successor
        tortoise = tortoise.successor
        if hare == tortoise:
            return True
    return False
```

Both of these functions take a head node of a linked list, and return True if there is a cycle in the linked list, and False otherwise. The time complexity of both functions is O(n), where n is the number of nodes in the linked list. The hash table method has an additional space complexity of O(n), to store the visited nodes in the hash table.