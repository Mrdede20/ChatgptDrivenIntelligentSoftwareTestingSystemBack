Here are two programs that achieve the intention of detecting if a linked list contains a cycle or not using the tortoise-and-hare algorithm:

First approach:
```python
def detect_cycle(head):
    tortoise = head
    hare = head

    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        if tortoise == hare:
            return True

    return False
```

Second approach:
```python
def detect_cycle(head):
    node_set = set()
    curr = head

    while curr is not None:
        if curr in node_set:
            return True
        node_set.add(curr)
        curr = curr.successor

    return False
```

These two implementations use different approaches to detect if there is a cycle in the linked list. The first approach uses two pointers, tortoise and hare, and checks if they meet at some point while traversing the linked list. The second approach uses a set to keep track of the visited nodes and returns True if a node is visited again. Both implementations have the same function name and input parameter type.