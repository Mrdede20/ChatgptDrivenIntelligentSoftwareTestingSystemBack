Here are two programs to detect cycle in a linked list using tortoise and hare method: 

Program 1:

```python
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
  
def detect_cycle(head):
    tortoise = hare = head
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        if tortoise == hare:
            return True
    return False
```

Program 2:

```python
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
    
def detect_cycle(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.successor:
        slow = slow.successor
        fast = fast.successor.successor
        if slow == fast:
            return True
    return False
```

Both programs follow the same approach that is tortoise and hare method to detect the cycle in the linked list. Program 1 has an additional attribute to keep track of the successors of the node, while program 2 has a condition to check if the head exists.