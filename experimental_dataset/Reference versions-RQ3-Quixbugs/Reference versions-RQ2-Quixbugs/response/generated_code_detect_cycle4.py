Program 1:

```python
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.successor:
        slow = slow.successor
        fast = fast.successor.successor
        if slow == fast:
            return True
    return False
```

Program 2:

```python
def has_cycle(head):
    visited = set()
    current = head
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.successor
    return False
```

Both programs achieve the same goal of detecting whether a linked list has a cycle or not, but use different approaches. The first program uses the "tortoise-and-hare" algorithm to move two pointers through the list, while the second program maintains a set of visited nodes and checks whether the current node has been visited before. Both algorithms have a time complexity of O(n) and a space complexity of O(n).