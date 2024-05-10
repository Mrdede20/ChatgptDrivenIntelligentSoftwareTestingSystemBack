Program 1:

```
def has_cycle(head):
    hare = tortoise = head
    while hare and hare.successor:
        hare = hare.successor.successor
        tortoise = tortoise.successor
        if hare == tortoise:
            return True
    return False
```

Program 2:

```
def has_cycle(head):
    hare = tortoise = head
    while hare and hare.successor:
        hare = hare.successor
        if hare == tortoise:
            return True
        hare = hare.successor
        tortoise = tortoise.successor
    return False
```

Note: Both of these programs have the same method name and parameter type, and use the Tortoise and Hare algorithm to detect cycles in a linked list. The difference between the two is in the way the pointers hare and tortoise are moved. The first program moves hare by two nodes and tortoise by one node, while the second program moves hare by one node and tortoise by one node. Both of them work fine in detecting cycles in a linked list.